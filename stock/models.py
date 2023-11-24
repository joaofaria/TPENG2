from django.db import models


class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=50)
    def __str__(self):
        return self.nome_categoria
    
class Produto(models.Model):
    nome_produto = models.CharField(max_length=50)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    quantidade_estoque = models.PositiveIntegerField(default = 0)
    valor_custo = models.FloatField(default=0)
    valor_venda = models.FloatField(default=0)
    disponivel = models.BooleanField(default=False)
    def __str__(self):
        return self.nome_produto
    