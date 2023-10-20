from django.shortcuts import render, redirect
from .models import Crianca
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def cadastro_crianca(request):
    return render(request, 'cadastro_crianca.html')

def listagem_crianca(request):
    if request.method == "POST":
        nova_crianca = Crianca()
        nova_crianca.nome = request.POST.get('nome')
        nova_crianca.idade = request.POST.get('idade')
        nova_crianca.nascimento = request.POST.get('nascimento')
        nova_crianca.status = request.POST.get('status')
        nova_crianca.periodo = request.POST.get('periodo')
        nova_crianca.entrada = request.POST.get('entrada')
        nova_crianca.permanencia = request.POST.get('permanencia')
        nova_crianca.turma = request.POST.get('turma')
        nova_crianca.autoavaliacao = request.POST.get('autoavaliacao')
        nova_crianca.faltas = request.POST.get('faltas')
        nova_crianca.save()
        
    try:
        context = {
            'criancas': Crianca.objects.all()
        }
        return render(request, 'criancas.html', context)
    except ObjectDoesNotExist:
        context['error'] = "Erro ao recuperar crianças do banco de dados."
        return render(request, 'criancas.html', context)

    

def info_crianca(request, crianca_id):
    crianca =  Crianca.objects.get(id_crianca=crianca_id)
    context = {'crianca': crianca}
    return render(request, 'info_crianca.html', context)
    

def home(request):
    return render(request, 'home.html')

def navbar(request):
    return render(request, 'navbar.html')
