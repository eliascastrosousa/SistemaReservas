from django.db import models


class Medico(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    crm = models.CharField(max_length=20, primary_key=True)
    datanasc = models.DateTimeField(null=True, blank=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    especialidade = models.CharField(max_length=100)
    cep = models.CharField(max_length=20)
    num = models.CharField(max_length=20)
    complemento = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Agenda(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    crm = models.CharField(max_length=10)
    data = models.DateField()
    horario = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Especialidade(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
