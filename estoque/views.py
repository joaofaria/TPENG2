from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Produto, Categoria
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required
def index(request):
    return render(request, 'estoque/index.html')

@login_required
def teste(request):
    return render(request, 'estoque/teste.html')

##### Cadastrar #####
class CategoriaCreate(LoginRequiredMixin, CreateView):
    model = Categoria
    fields = ['nome_categoria']
    template_name = 'estoque/form.html'
    success_url = reverse_lazy('produtos')

class ProdutoCreate(LoginRequiredMixin, CreateView):
    model = Produto
    fields = ['nome_produto', 'categoria', 'quantidade_estoque', 'valor_custo', 'valor_venda', 'disponivel']
    template_name = 'estoque/form.html'
    success_url = reverse_lazy('produtos')

##### Editar #####

class CategoriaUpdate(LoginRequiredMixin, UpdateView):
    model = Categoria
    fields = ['nome_categoria']
    template_name = 'estoque/form.html'
    success_url = reverse_lazy('produtos')

class ProdutoUpdate(LoginRequiredMixin, UpdateView):
    model = Produto
    fields = ['nome_produto', 'categoria', 'quantidade_estoque', 'valor_custo', 'valor_venda', 'disponivel']
    template_name = 'estoque/form.html'
    success_url = reverse_lazy('produtos')

##### Excluir #####
class CategoriaDelete(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = 'estoque/form-excluir.html'
    success_url = reverse_lazy('produtos')

class ProdutoDelete(LoginRequiredMixin, DeleteView):
    model = Produto
    template_name = 'estoque/form-excluir.html'
    success_url = reverse_lazy('produtos')

##### Visualizar #####
class ProdutoList(LoginRequiredMixin, ListView):
    model = Produto
    template_name = 'estoque/produtos.html'
    success_url = reverse_lazy('produtos')