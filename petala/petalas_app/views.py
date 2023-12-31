from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Crianca, Doacao, Presenca
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def cadastro_crianca(request, turma_atual):
    if request.method == "GET":
        context = {
            'turma' : turma_atual
        }
        return render(request, 'cadastro_crianca.html', context)
    else:
        nova_crianca = Crianca()
        nova_crianca.nome = request.POST.get('nome')
        nova_crianca.idade = request.POST.get('idade')
        nova_crianca.nascimento = request.POST.get('nascimento')
        nova_crianca.entrada = request.POST.get('entrada')
        nova_crianca.turma = turma_atual
        nova_crianca.cpf_crianca = request.POST.get('cpf_crianca')
        nova_crianca.nome_resp = request.POST.get('nome_resp')
        nova_crianca.cpf_resp = request.POST.get('cpf_resp')
        nova_crianca.email_resp = request.POST.get('email_resp')
        nova_crianca.tel_resp = request.POST.get('tel_resp')
        nova_crianca.save()
        
        try:
            context = {
                'criancas': Crianca.objects.filter(turma = turma_atual),
                'turma' : turma_atual,
            }
            return render(request, 'criancas.html', context)
        except ObjectDoesNotExist:
            context['error'] = "Erro ao recuperar crianças do banco de dados."
            return render(request, 'criancas.html', context)
        
        

def listagem_crianca(request, turma_atual):
    context = {
        'criancas' : Crianca.objects.filter(turma = turma_atual),
        'turma' : turma_atual,
    }
    return render(request, 'criancas.html', context)

    

def info_crianca(request, crianca_id):
    crianca =  Crianca.objects.get(id_crianca=crianca_id)
    context = {'crianca': crianca}
    return render(request, 'info_crianca.html', context)
    

def home(request):
    return render(request, 'home.html')

def navbar(request):
    return render(request, 'navbar.html')

def listagem_doacao(request):
    if request.method == 'POST':
        nova_doacao = Doacao()
        nova_doacao.nome_padrinho = request.POST.get('nome_padrinho')
        nova_doacao.valor = request.POST.get('valor')
        nova_doacao.cpf = request.POST.get('cpf')
        nova_doacao.destino = request.POST.get('nome_crianca')
        nova_doacao.tipo = request.POST.get('descricao')
        nova_doacao.save()

    try:
        context = {
            'doacoes': Doacao.objects.all()
        }

        return render(request, 'doacoes.html', context)
    except ObjectDoesNotExist:
        context['error'] = "Erro ao recuperar doações do banco de dados."
        return render(request, 'doacoes.html', context)
        

def cadastro_doacao(request):
    return render(request, 'cadastro_doacao.html')
        
def info_doacao(request, doacao_id):
    doacao =  Doacao.objects.get(id_doacao=doacao_id)
    context = {'doacao': doacao}
    return render(request, 'info_doacao.html', context)

def listagem_turmas(request):
    turmas = ["Eu e o Mundo - Manhã", "Nós e o Mundo - Manhã", "Eu e o Mundo - Tarde", "Nós e o Mundo - Tarde"]
    context = {
        'turmas' : turmas,
        'turmaA' : turmas[0],
        'turmaB' : turmas[1],
        'turmaC' : turmas[2],
        'turmaD' : turmas[3],
    }
    return render(request, 'turmas.html', context)

def resultado_pesquisa(request):
    if request.method == "GET":
        busca = request.GET.get("pesquisa")

        resultados_crianca = Crianca.objects.filter(nome__icontains=busca)
        resultados_doacao = Doacao.objects.filter(nome_padrinho__icontains=busca)

        context = {
            'resultados_crianca': resultados_crianca,
            'resultados_doacao': resultados_doacao,
            'busca': busca,
        }

        return render(request, 'resultado_pesquisa.html', context)
    
def acesso_crianca(request, id_field):
    id_crianca = Crianca.objects.get(id_crianca = id_field)
    context = {'crianca': id_crianca}
    return render(request, 'acesso_pesquisa.html', context)

def acesso_doacao(request, id_field):
    id_doacao = Doacao.objects.get(id_doacao = id_field)
    context = {'doacao': id_doacao,}
    return render(request, 'acesso_pesquisa.html', context)


def cadastro_presenca(request, turma_atual):
    if request.method == "GET":
        criancas = Crianca.objects.filter(turma=turma_atual)
        context = {
            'turma' : turma_atual,
            'criancas': criancas,
        }
        return render(request, 'cadastro_presenca.html', context)
    else:
        data = request.POST.get('data')
        criancas_presentes = request.POST.getlist('criancas_presentes')

        nova_presenca = Presenca(
            data=data,
            turma=turma_atual,
            crianca_nome=', '.join(criancas_presentes),
            presentes = True
        )

        nova_presenca.save()
        
        try:
            context = {
                'presencas': Presenca.objects.filter(turma=turma_atual),
                'turma': turma_atual,
            }
            return render(request, 'presencas.html', context)
        except ObjectDoesNotExist:
            context['error'] = "Erro ao recuperar lista de presença do banco de dados."
            return render(request, 'presencas.html', context)


def listagem_presenca(request, turma_atual):
    context = {
        'presencas' : Presenca.objects.filter(turma = turma_atual),
        'turma' : turma_atual,
        'turma_url': reverse('listagem_criancas', kwargs={'turma_atual': turma_atual}),
    }
    return render(request, 'presencas.html', context)


def info_presenca(request, presenca_id):
    presenca =  Presenca.objects.get(id_presenca=presenca_id)
    context = {'presenca': presenca}
    return render(request, 'info_presenca.html', context)