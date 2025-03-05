from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=100, null=True)
    cargo = models.CharField(max_length=100, null=True)
    codigo_funcional = models.CharField(max_length=100, null=True)
    nascimento = models.DateField(null=True)
    tipo_cargo = models.CharField(max_length=100, null=True)
    data_admissao = models.DateField(null=True)
    data_saida = models.DateField(null=True)
