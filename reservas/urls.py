
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    
    path('patientlist', views.patientlist, name='patientlist'),
    path('patientregister', views.patientregister, name='patientregister'),
    path('patientsearch', views.patientsearch, name='patientsearch'),
    path('cadastrar_paciente', views.cadastrar_paciente, name='cadastrar_paciente'),

    path('schedulinglist', views.schedulinglist, name='schedulinglist'),
    path('schedulingregister', views.schedulingregister, name='schedulingregister'),
    path('schedulingsearch', views.schedulingsearch, name='schedulingsearch'),
    
    path('professionallist', views.professionallist, name='professionallist'),
    path('professionalregister', views.professionalregister, name='professionalregister'),
    path('professionalsearch', views.professionalsearch, name='professionalsearch'),
    path('professionalagend', views.professionalagend, name='professionalagend'),
    path('cadastrar_medico', views.cadastrar_medico, name='cadastrar_medico'),
    path('specialtyregister', views.specialtyregister, name='specialtyregister'),
    path('cadastrar_especialidade', views.cadastrar_especialidade, name='cadastrar_especialidade')
    

    
]
