from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Produto, Categoria
from .forms import CategoriaForm, ProdutoForm
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
    form_class = CategoriaForm
    permission_required = "estoque.add_categoria"
    template_name = 'estoque/form.html'
    success_url = reverse_lazy('produtos')
    success_message = "Categoria criada com sucesso!"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastrar Categoria'
        return context

class ProdutoCreate(PermissionRequiredMixin, CreateView):
    login_url = reverse_lazy('login')   
    model = Produto
    form_class = ProdutoForm
    permission_required = "estoque.add_produto"
    template_name = 'estoque/form.html'
    success_url = reverse_lazy('produtos')
    success_message = "Produto criado com sucesso!"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastrar Produto'
        return context    

##### Editar #####

class CategoriaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Categoria
    form_class = CategoriaForm
    template_name = 'estoque/form.html'
    success_url = reverse_lazy('produtos')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Categoria'
        return context

class ProdutoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Produto
    form_class = ProdutoForm
    template_name = 'estoque/form.html'
    success_url = reverse_lazy('produtos')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Produto'
        return context
    
##### Excluir #####
class CategoriaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Categoria
    template_name = 'estoque/form-excluir.html'
    success_url = reverse_lazy('produtos')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Excluir Categoria'
        return context
    
class ProdutoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Produto
    template_name = 'estoque/form-excluir.html'
    success_url = reverse_lazy('produtos')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Excluir Produto'
        return context
    
##### Visualizar #####
class ProdutoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Produto
    template_name = 'estoque/produtosList.html'
    permission_required = "estoque.view_produto"
    success_url = reverse_lazy('produtos')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Produtos'
        return context

class CategoriaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Categoria
    template_name = 'estoque/categoriasList.html'
    permission_required = "estoque.view_categoria"
    success_url = reverse_lazy('produtos')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Categorias'
        return context
