from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Produto, Categoria
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

@login_required
def index(request):
    return render(request, 'estoque/index.html')

@login_required
def teste(request):
    return render(request, 'estoque/teste.html')

##### Cadastrar #####
class CategoriaCreate(PermissionRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Categoria
    permission_required = "estoque.add_categoria"
    fields = ['nome_categoria']
    template_name = 'estoque/form.html'
    success_url = reverse_lazy('produtos')

class ProdutoCreate(PermissionRequiredMixin, CreateView):
    login_url = reverse_lazy('login')   
    model = Produto
    permission_required = "estoque.add_produto"
    fields = ['nome_produto', 'categoria', 'quantidade_estoque', 'valor_custo', 'valor_venda', 'disponivel']
    template_name = 'estoque/form.html'
    success_url = reverse_lazy('produtos')

##### Editar #####

class CategoriaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Categoria
    fields = ['nome_categoria']
    template_name = 'estoque/form.html'
    success_url = reverse_lazy('produtos')

class ProdutoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Produto
    fields = ['nome_produto', 'categoria', 'quantidade_estoque', 'valor_custo', 'valor_venda', 'disponivel']
    template_name = 'estoque/form.html'
    success_url = reverse_lazy('produtos')

##### Excluir #####
class CategoriaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Categoria
    template_name = 'estoque/form-excluir.html'
    success_url = reverse_lazy('produtos')

class ProdutoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Produto
    template_name = 'estoque/form-excluir.html'
    success_url = reverse_lazy('produtos')

##### Visualizar #####
class ProdutoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Produto
    template_name = 'estoque/produtos.html'
    success_url = reverse_lazy('produtos')