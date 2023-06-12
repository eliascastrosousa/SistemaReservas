from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=20, primary_key=True)
    datanasc = models.DateTimeField(null=True, blank=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    cep = models.CharField(max_length=20)
    num = models.CharField(max_length=20)
    complemento = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
