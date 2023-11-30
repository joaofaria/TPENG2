from django.db import models


class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=50)
    def __str__(self):
        return self.nome_categoria
    
class Produto(models.Model):
    nome_produto = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    quantidade_estoque = models.PositiveIntegerField(default = 0)
    valor_custo = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    valor_venda = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    disponivel = models.BooleanField(default=False)
    imagem_produto = models.ImageField(upload_to='produtos/', null=True, blank=True)  # Adiciona o campo de imagem
    
    def __str__(self):
        return self.nome_produto
    