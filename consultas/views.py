from django.shortcuts import render, redirect
from .models import Consulta, Medico, Paciente, Agenda, Especialidade
from medicos.views import Medico, Especialidade
from pacientes.views import Paciente


# Create your views here.

def schedulinglist(request):
    consulta = Consulta.objects.all()
    return render(request, 'schedulinglist.html', {"consulta":consulta})


def schedulingsearch(request):
    txt_search = request.GET.get('search')
    if txt_search:
        
        if Consulta.objects.filter(nome__icontains = txt_search):
            consultas = Consulta.objects.filter(nome_paciente__icontains = txt_search)
        elif Consulta.objects.filter(sobrenome__icontains = txt_search):
            consultas = Consulta.objects.filter(cpf__icontains = txt_search)
        elif Consulta.objects.filter(cpf__icontains = txt_search):
            consultas = Consulta.objects.filter(id__icontains = txt_search)
        
        return render(request, 'schedulinglist.html', {"consulta":consultas} )
    else:
        consultas = Paciente.objects.all()
    return render(request, 'schedulinglist.html', {"consulta":consultas} )


def schedulingregister(request):
    agenda = Agenda.objects.all()
    paciente = Paciente.objects.all()
    especialidades = Especialidade.objects.all()
    medico = Medico.objects.all()
    return render(request, 'schedulingregister.html', {"especialidades":especialidades, "medico":medico,"agenda":agenda} )

def schedulingregistersearchpatient(request):
    txt_search = request.GET.get('search')
    especialidades = Especialidade.objects.all()
    medico = Medico.objects.all()
    agenda = Agenda.objects.all()
    if txt_search:
        if Paciente.objects.filter(nome__icontains = txt_search):
            paciente = Paciente.objects.filter(nome__icontains = txt_search)
        elif Paciente.objects.filter(sobrenome__icontains = txt_search):
            paciente = Paciente.objects.filter(sobrenome__icontains = txt_search)
        elif Paciente.objects.filter(cpf__icontains = txt_search):
            paciente = Paciente.objects.filter(cpf__icontains = txt_search)
        
        return render(request, 'schedulingregister.html', {"especialidades":especialidades, "medico":medico,"paciente":paciente, "agenda":agenda} )
    else:
        paciente = Paciente.objects.all()
    return render(request, 'schedulingregister.html', {"especialidades":especialidades, "medico":medico, "paciente":paciente,"agenda":agenda} )

def saveconsulting(request):
    crm = request.POST.get('crm')
    cpf = request.POST.get('cpf')
    data = request.POST.get('data')
    horario = request.POST.get('horario')
    
    Consulta.objects.create(
        crm = crm,
        cpf = cpf,
        data = data,
        horario = horario
    )

    return redirect(schedulinglist)
