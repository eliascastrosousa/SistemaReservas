from django.shortcuts import render, redirect
from .models import Medico, Especialidade, Agenda


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
    return redirect(specialtyregister)

def professionalagend(request):
    medicos = Medico.objects.all()
    return render(request, 'professionalagend.html',{"medicos":medicos})

def agendmentlist(request):
    agenda = Agenda.objects.all()
    return render(request, 'agendmentlist.html',{"agenda":agenda})

def agendmentsearch(request):
    search = request.GET.get('search')
    agenda = Agenda.objects.filter(nome__icontains = search)
    return render(request, 'agendmentlist.html', {"agenda":agenda})

def saveprofessionalagend(request):
    nomemedico = request.POST.get('nome')
    data = request.POST.get('data')
    horario = request.POST.get('horario')
    crm = ''

    medicos = Medico.objects.all()

    for item in medicos:
        if nomemedico == item.nome:
            crm = item.crm
            break

    Agenda.objects.create(
        nome = nomemedico,
        crm = crm,
        data = data,
        horario = horario
    )

    return redirect(agendmentlist)
