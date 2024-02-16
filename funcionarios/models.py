from django.db import models
from administracao.models import Loja

class Funcionario(models.Model):

    def __str__(self):
        return self.nome_funcionario
    
    