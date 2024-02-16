from django import forms
from django.contrib.auth.models import User
from .models import Venda, ItemVenda
from estoque.models import Produto
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

class ItemVendaForm(forms.ModelForm):
    class Meta:
        model = ItemVenda
        exclude = []  # Remova a linha 'fields'

class VendaForm(forms.ModelForm):
    produtos = forms.ModelMultipleChoiceField(
        queryset=Produto.objects.all(),
        widget=forms.CheckboxSelectMultiple,  # Use widgets adequados para múltipla escolha
    )
    
    funcionario = forms.ModelChoiceField(
        queryset=User.objects.filter(is_staff=False),
    )

    class Meta:
        model = Venda
        fields = ['funcionario', 'total']

class VendaCreate(CreateView):
    model = Venda
    form_class = VendaForm  # Usando o formulário personalizado
    template_name = 'vendas/form.html'
    success_url = reverse_lazy('lista-vendas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['produtos_disponiveis'] = Produto.objects.all()
        return context

    def form_valid(self, form):
        produtos_selecionados = self.request.POST.getlist('produtos')
        form.instance.produtos.set(produtos_selecionados)
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Passando o usuário atual para o formulário
        return kwargs

    def get_queryset(self):
        return User.objects.filter(is_staff=False)

class VendaUpdateForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['funcionario', 'total']  # Adicione os campos desejados
