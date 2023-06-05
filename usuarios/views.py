from django.shortcuts import render
import requests



def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def authtwofactor(request):
    return render(request, 'authtwofactor.html')

def validacep(request):
    cep = "07082560"
    link = f'https://viacep.com.br/ws/{cep}/json/'
    requisicao = requests.get(link)
    print(requisicao)
    dic_requisicao = requisicao.json()
    cidade = dic_requisicao['localidade']
    uf = dic_requisicao['uf']
    bairro = dic_requisicao['bairro']
    print(requisicao.json())
    print(cidade, uf, bairro)

def perfil(request):
    return render(request, 'perfil.html')