from django.contrib import admin

from .models import Medico, Agenda, Especialidade

admin.site.register(Medico)
admin.site.register(Agenda)
admin.site.register(Especialidade)
