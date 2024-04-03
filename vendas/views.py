# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, View
from django.urls import reverse_lazy
from .models import Venda, ItemVenda
from estoque.models import Produto
from django.contrib.auth.models import User
from .forms import VendaForm, VendaUpdateForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt  # Adicione esta linha
import json
from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.db.models.functions import ExtractDay, ExtractMonth

def index(request):
    return render(request, 'POSmart/index.html')

class VendaList(ListView):
    model = Venda
    template_name = 'vendas/vendas.html'
    context_object_name = 'vendas'

    def get_queryset(self):
        # Modificamos o queryset para incluir os itens da venda
        return Venda.objects.prefetch_related('itemvenda_set__produto').all()
class VendaCreate(CreateView):
    model = Venda
    form_class = VendaForm  # Corrigir o nome do formulário personalizado

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Adicionar Venda'
        context['produtos_disponiveis'] = Produto.objects.all()
        return context

    def form_valid(self, form):
        produtos_selecionados = self.request.POST.getlist('produtos')
        form.instance.produtos.set(produtos_selecionados)
        return super().form_valid(form)

    template_name = 'vendas/form.html'
    success_url = reverse_lazy('vendas')


class VendaUpdate(UpdateView):
    model = Venda
    form_class = VendaUpdateForm
    template_name = 'vendas/form.html'
    success_url = reverse_lazy('vendas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        venda = self.get_object()

        # Obtém todos os itens da venda
        itens_venda = venda.itemvenda_set.all()

        # Obtém os produtos associados aos itens da venda
        produtos_selecionados = [item.produto.id for item in itens_venda]

        # Adiciona os produtos disponíveis e selecionados ao contexto
        context['produtos_selecionados'] = produtos_selecionados
        context['produtos_disponiveis'] = Produto.objects.all()

        return context

    def form_valid(self, form):
        produtos_selecionados = self.request.POST.getlist('produtos')

        # Limpe os itens existentes da venda
        self.object.itemvenda_set.all().delete()

        # Adicione os novos itens à venda
        for produto_id in produtos_selecionados:
            quantidade = self.request.POST.get(f'quantidade_{produto_id}')
            produto = Produto.objects.get(pk=produto_id)

            item_venda = ItemVenda.objects.create(produto=produto, quantidade=quantidade, venda=self.object)
            item_venda.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        # Adicione manipulação para lidar com formulário inválido, se necessário
        return self.render_to_response(self.get_context_data(form=form))

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return self.render_to_response(self.get_context_data())

class VendaDelete(DeleteView):
    model = Venda
    template_name = 'vendas/form-excluir.html'
    success_url = reverse_lazy('vendas')  # Substitua 'lista-vendas' pelo nome da URL da lista de vendas


class VendaView(View):
    template_name = 'vendas/sistema.html'

    def get(self, request, *args, **kwargs):
        produtos = Produto.objects.all()
        return render(request, self.template_name, {'produtos': produtos})
    

@csrf_exempt  # Aplique o decorador csrf_exempt
@require_POST
def buscar_produto(request):
    codigo_barras = request.POST.get('codigo_barras')
    try:
        produto = Produto.objects.get(codigo_barras=codigo_barras)
        data = {'id': produto.id, 'nome': produto.nome_produto, 'preco': str(produto.valor_venda).replace('.', ',')}
        return JsonResponse(data)
    except Produto.DoesNotExist:
        return JsonResponse({'error': 'Produto não encontrado'}, status=404)
    

@csrf_exempt
@require_POST
@login_required
def finalizar_venda(request):
    try:
        # Obtém os dados do corpo da solicitação como JSON
        data = json.loads(request.body.decode('utf-8'))

        carrinho = data.get('carrinho', [])
        formas_pagamento = data.get('formas_pagamento', [])
        usuario_logado = data.get('usuario_logado', '')

        print('Formas de Pagamento:', formas_pagamento)

        # Obtém o usuário logado
        usuario = request.user

        # Crie uma instância de Venda associada ao usuário com total inicial zero
        venda = Venda.objects.create(total=0, funcionario=usuario, formas_pagamento=str(formas_pagamento))

        # Percorre os itens do carrinho
        for item in carrinho:
            # Separa o ID do produto e a quantidade
            produto_id, quantidade = map(int, item.split('-'))

            # Obtém o produto do banco de dados
            produto = Produto.objects.get(pk=produto_id)

            # Cria uma instância de ItemVenda associada à venda e ao produto
            item_venda = ItemVenda.objects.create(produto=produto, quantidade=quantidade, venda=venda)

            # Atualiza o estoque do produto
            produto.quantidade_estoque -= quantidade
            produto.save()

        # Calcula o total da venda
        total_venda = sum(item.produto.valor_venda * item.quantidade for item in venda.itemvenda_set.all())
        
        # Atualiza o total da venda na instância de Venda
        venda.total = total_venda
        venda.save()

        # Retorna uma resposta de sucesso
        return JsonResponse({'success': 'Venda finalizada com sucesso'})
    except Exception as e:
        return JsonResponse({'error': str(e)})

class RelatorioVendasDiaMesView(View):
    def get(self, request):
        # Obter dados agregados de vendas por dia/mês
        vendas_por_dia_mes = Venda.objects.annotate(
            dia=ExtractDay('data_venda'),
            mes=ExtractMonth('data_venda')
        ).values('dia', 'mes').annotate(
            total_vendas=Sum('total')
        ).order_by('mes', 'dia')

        context = {'vendas_por_dia_mes': vendas_por_dia_mes}
        return render(request, 'vendas/relatorio_vendas_dia_mes.html', context)

class RelatorioVendasFuncionarioMesView(View):
    template_name = 'vendas/relatorio_vendas_funcionario_mes.html'

    def get(self, request, *args, **kwargs):
        vendas_por_funcionario_mes = Venda.objects \
            .values('funcionario__username', 'data_venda__month') \
            .annotate(total_vendas=Sum('total'))

        print(vendas_por_funcionario_mes)  # Adicione esta linha para debug

        context = {
            'vendas_por_funcionario_mes': vendas_por_funcionario_mes,
            'data_venda_month': 'data_venda__month'  # Adicione isso ao contexto
        }

        # Renderizar o template com o contexto
        return render(request, self.template_name, context)
class RelatoriosView(View):
    template_name = 'vendas/relatoriosMain.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
import os
from django.shortcuts import redirect

def encerrar_servidor(request):
    os._exit(0)  # Encerra o servidor