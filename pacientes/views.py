from django.shortcuts import render, redirect
from .models import  Paciente

# Create your views here.

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

def patientsearch( request):
    txt_search = request.GET.get('search')
    if txt_search:
        
        if Paciente.objects.filter(nome__icontains = txt_search):
            paciente = Paciente.objects.filter(nome__icontains = txt_search)
        elif Paciente.objects.filter(sobrenome__icontains = txt_search):
            paciente = Paciente.objects.filter(sobrenome__icontains = txt_search)
        elif Paciente.objects.filter(cpf__icontains = txt_search):
            paciente = Paciente.objects.filter(cpf__icontains = txt_search)
        
        return render(request, 'patientlist.html', {"paciente":paciente} )
    else:
        paciente = Paciente.objects.all()
    return render(request, 'patientlist.html', {"paciente":paciente} )
