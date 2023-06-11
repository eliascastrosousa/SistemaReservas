from django.shortcuts import render, redirect
from .models import Medico, Paciente, Especialidade, Agenda, Consulta

# Create your views here.

def home(request):
    return render(request, 'home.html')

#Pacientes
def patientlist(request):
    paciente = Paciente.objects.all()
    return render(request, 'patientlist.html',{"paciente":paciente})

def patientregister(request):
    return render(request, 'patientregister.html')

def cadastrar_paciente(request):
       nome = request.POST.get('nome')
       sobrenome = request.POST.get('sobrenome')
       cpf = request.POST.get('cpf')
       datanasc = request.POST.get('datanasc')
       email = request.POST.get('email')
       telefone = request.POST.get('telefone')
       cep = request.POST.get('cep')
       num = request.POST.get('num')
       complemento = request.POST.get('complemento')

       paciente = Paciente.objects.all()
       Paciente.objects.create(
           nome = nome,
           sobrenome = sobrenome,
           cpf = cpf,
           datanasc = datanasc,
           email = email,
           telefone = telefone,
           cep = cep,
           num = num,
           complemento = complemento
       )

       return redirect(patientlist)

def patientsearch(request):
    search = request.GET.get('search')
    paciente = Paciente.objects.filter(nome__icontains = search)
    return render(request, 'patientlist.html', {"paciente": paciente})

#agendamentos
def schedulinglist(request):
    consulta = Consulta.objects.all()
    return render(request, 'schedulinglist.html', {"consulta":consulta})

def schedulingregister(request):
    paciente = Paciente.objects.all()
    especialidades = Especialidade.objects.all()
    medico = Medico.objects.all()
    return render(request, 'schedulingregister.html', {"especialidades":especialidades, "medico":medico, "paciente":paciente} )

def schedulingsearch(request):
    search = request.GET.get('search')
    consultas = Consulta.objects.filter(nome__icontains = search)
    return render(request, 'schedulinglist.html', {"consulta": consultas})

def professionallist(request):
    medico = Medico.objects.all()
    return render(request, 'professionallist.html', {"medicos":medico})

def professionalregister(request):
    especialidades = Especialidade.objects.all()
    return render(request, 'professionalregister.html', {"especialidades":especialidades})

def professionalsearch(request):
    search = request.GET.get('search')
    medicos = Medico.objects.filter(nome__icontains = search)
    return render(request, 'professionallist.html', {"medicos":medicos})

def professionalagend(request):
    medicos = Medico.objects.all()
    return render(request, 'professionalagend.html',{"medicos":medicos})

def cadastrar_medico(request):
       nome = request.POST.get('nome')
       sobrenome = request.POST.get('sobrenome')
       datanasc = request.POST.get('datanasc')

       crm = request.POST.get('crm')
       email = request.POST.get('email')
       telefone = request.POST.get('telefone')
       especialidade = request.POST.get('especialidade')
       cep = request.POST.get('cep')
       num = request.POST.get('num')
       complemento = request.POST.get('complemento')

       medico = Medico.objects.all()
       Medico.objects.create(
           nome = nome,
           sobrenome = sobrenome,
           datanasc = datanasc,
           crm = crm,
           email = email,
           telefone = telefone,
           especialidade = especialidade,
           cep = cep,
           num = num,
           complemento = complemento
       )

       return redirect(professionallist)


def specialtyregister(request):
     especialidades = Especialidade.objects.all()
     return render(request, 'specialtyregister.html', {"especialidades":especialidades})
    
def cadastrar_especialidade(request):
    nome = request.POST.get('nome')
    Especialidade.objects.create(
        nome = nome)
    return redirect(professionallist)
