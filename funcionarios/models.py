from django.db import models
from administracao.models import Loja

class Funcionario(models.Model):
    nome_funcionario = models.CharField(max_length=50)
    telefone_funcionario = models.CharField(max_length=20, default='(00)00000-0000')
    cpf_funcionario = models.CharField(max_length=20, unique=True, default='000.000.000-00')
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE, related_name='funcionarios', default=1)
    
    def __str__(self):
        return self.nome_funcionario