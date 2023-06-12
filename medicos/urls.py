from . import views
from django.urls import path

urlpatterns = [
    path('', views.professionallist, name='professionallist'),
    path('professionallist', views.professionallist, name='professionallist'),
    path('professionalregister', views.professionalregister, name='professionalregister'),
    path('professionalsearch', views.professionalsearch, name='professionalsearch'),
    path('professionalagend', views.professionalagend, name='professionalagend'),
    path('cadastrar_medico', views.cadastrar_medico, name='cadastrar_medico'),
    path('specialtyregister', views.specialtyregister, name='specialtyregister'),
    path('cadastrar_especialidade', views.cadastrar_especialidade, name='cadastrar_especialidade'),
    path('saveprofessionalagend', views.saveprofessionalagend, name='saveprofessionalagend'),
    path('agendmentlist', views.agendmentlist, name='agendmentlist'),
    path('agendmentsearch', views.agendmentsearch, name='agendmentsearch')

    
]