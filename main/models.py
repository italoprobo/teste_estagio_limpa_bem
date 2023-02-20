from django.db import models
from django.contrib.auth.models import User

class Servico(models.Model):
    nome = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Atendimento(models.Model):
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    atendente = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name='atendimentos_feitos')
    helper = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name='atendimentos_executados')
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    desconto = models.DecimalField(max_digits=6, decimal_places=2)
    forma_pagamento = models.CharField(max_length=50)
    data_cadastro = models.DateTimeField()
    data_execucao = models.DateTimeField()
    situacao = models.CharField(max_length=50)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return self.servico.nome
        



# Create your models here.
