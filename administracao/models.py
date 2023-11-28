from django.db import models
from django.contrib.auth.models import User

class Loja(models.Model):
    nome_loja = models.CharField(max_length=100)
    usuario_responsavel = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    cnpj_loja = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.nome_loja