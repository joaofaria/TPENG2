from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.models import User, Group
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import UsuarioCreationForm, UsuarioChangeForm, GroupCreationForm

@login_required
def index(request):
    return render(request, 'funcionarios/index.html')

##### Criar #####
class UsuarioCreate(LoginRequiredMixin, CreateView):
    template_name = "funcionarios/form.html"
    permission_required = "auth.add_user"
    form_class = UsuarioCreationForm
    success_url = reverse_lazy("equipe")
    login_url = reverse_lazy('login')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Registro de Novo Usuário"
        context['subtitulo'] = "Preencha os campos abaixo para cadastrar um novo usuário"
        return context

##### Editar #####
class UsuarioUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = User
    template_name = "funcionarios/form.html"
    form_class = UsuarioChangeForm
    success_url = reverse_lazy("equipe")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Editar Usuário"
        context['subtitulo'] = "Preencha os campos abaixo para cadastrar um novo usuário"
        return context

##### Visualizar #####
class UsuariosList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = User
    permission_required = "auth.view_user"
    template_name = 'funcionarios/funcionariosList.html'
    context_object_name = 'usuarios'

    def get_queryset(self):
        # Exclua o usuário administrador da lista
        return User.objects.filter(is_staff=False)


##### Excluir #####
class UsuarioDelete(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "funcionarios/form-excluir.html"  # Substitua com o seu template de confirmação de exclusão
    success_url = reverse_lazy("equipe")
    login_url = reverse_lazy('login')

class GrupoCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Group
    template_name = "funcionarios/form.html"
    form_class = GroupCreationForm
    permission_required = "auth.add_group"
    success_url = reverse_lazy("grupos")
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Registro de Novo Grupo"
        context['subtitulo'] = "Preencha os campos abaixo para cadastrar um novo grupo"
        return context

class GrupoUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Group
    template_name = "funcionarios/form.html"
    form_class = GroupCreationForm
    permission_required = "auth.change_group"
    success_url = reverse_lazy("grupos")
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Editar Grupo"
        context['subtitulo'] = "Atualize os detalhes do grupo"
        return context

class GruposList(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Group
    permission_required = "auth.view_group"
    template_name = 'funcionarios/gruposList.html'
    context_object_name = 'grupos'

class GrupoDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'auth.delete_group'
    model = Group
    template_name = "funcionarios/form-excluir.html"
    success_url = reverse_lazy("grupos")
    login_url = reverse_lazy('login')