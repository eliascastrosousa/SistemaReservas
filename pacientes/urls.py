
from . import views
from django.urls import path

urlpatterns = [
    path('', views.patientlist, name='patientlist'),
    path('patientlist', views.patientlist, name='patientlist'),
    path('patientregister', views.patientregister, name='patientregister'),
    path('patientsearch', views.patientsearch, name='patientsearch'),
    path('cadastrar_paciente', views.cadastrar_paciente, name='cadastrar_paciente')
]