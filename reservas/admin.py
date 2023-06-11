from django.contrib import admin
from .models import Medico, Paciente, Agenda, Consulta, Especialidade

admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Agenda)
admin.site.register(Consulta)
admin.site.register(Especialidade)

