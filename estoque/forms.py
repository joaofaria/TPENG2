from django import forms
from .models import Categoria, Produto

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome_categoria']

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome_produto', 'categoria',  'codigo_barras','quantidade_estoque', 'valor_custo', 'valor_venda', 'disponivel', 'imagem_produto']
    