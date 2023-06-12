from django.db import models
from medicos.models import Medico, Especialidade, Agenda
from pacientes.models import Paciente

class Consulta(models.Model):
    crm = models.ForeignKey(Medico, on_delete=models.CASCADE)
    cpf = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.CharField(max_length=20)

    def __str__(self):
        return self.id
