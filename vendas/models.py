# models.py
from django.db import models
from estoque.models import Produto
from django.contrib.auth.models import User
from django.utils import timezone

class Venda(models.Model):
    total = models.DecimalField(decimal_places=2, max_digits=10)
    data_venda = models.DateField(auto_now_add=True)
    funcionario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    formas_pagamento = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.funcionario} - {self.data_venda}"

class ItemVenda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, null=True, default=None)
