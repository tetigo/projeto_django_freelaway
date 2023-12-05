from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Jobs, Referencias
from datetime import datetime
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.models import User


# Create your views here.
def encontrar_jobs(req):
    if not req.user.is_authenticated:
        return redirect('/auth/login')
    if req.method == 'GET':
        jobs = Jobs.objects.filter(reservado=False)
        return render(req, 'encontrar_jobs.html',context={'jobs': jobs})

    if req.method == 'POST':
        preco_minimo = req.POST.get('preco_minimo')
        preco_maximo = req.POST.get('preco_maximo')
        prazo_minimo = req.POST.get('prazo_minimo')
        prazo_maximo = req.POST.get('prazo_maximo')
        categoria = req.POST.get('categoria')
        
        if not preco_minimo: preco_minimo = 0
        if not preco_maximo: preco_maximo = 999999
        if not prazo_minimo: prazo_minimo = datetime(year=2023, month=1, day=1)
        if not prazo_maximo: prazo_maximo = datetime(year=2123, month=1, day=1)
        
        jobs = Jobs.objects.filter(reservado=False)\
                            .filter(preco__gte = preco_minimo)\
                            .filter(preco__lte = preco_maximo)\
                            .filter(prazo_entrega__gte = prazo_minimo)\
                            .filter(prazo_entrega__lte = prazo_maximo)
        
        if categoria != 'T':
            jobs = jobs.filter(categoria = categoria)
        
        return render(req, 'encontrar_jobs.html',context={'jobs': jobs})
    
    

def aceitar_job(req, id):
    if not req.user.is_authenticated:
        return redirect('/auth/login')
    try:
        job = Jobs.objects.get(id=id)
        if not job:
            messages.add_message(req, constants.ERROR, 'Job não encontrado')
            return redirect('/jobs/encontrar_jobs')
        job.profissional = req.user
        job.reservado = True
        job.save()
        messages.add_message(req, constants.SUCCESS, 'Job reservado com sucesso')
        return redirect('/jobs/encontrar_jobs')
    except:
        messages.add_message(req, constants.ERROR, 'Erro interno do sistema')
        return redirect('/jobs/encontrar_jobs')


def perfil(req):
    if not req.user.is_authenticated:
        return redirect('/auth/login')
    
    if req.method == 'GET':
        jobs = Jobs.objects.filter(profissional = req.user)
        return render(req, 'perfil.html', {'jobs':jobs})
    
    if req.method == 'POST':
        try:
            username = req.POST.get('username')
            email = req.POST.get('email')
            first_name = req.POST.get('primeiro_nome')
            last_name = req.POST.get('ultimo_nome')
            
            usuario = User.objects.filter(username=username).exclude(id = req.user.id)
            
            if usuario.exists():
                messages.add_message(req, constants.ERROR, 'Usuário já existe com esse username')
                return redirect('/jobs/perfil')
            
            usuario = User.objects.filter(email=email).exclude(id = req.user.id)
            
            if usuario.exists():
                messages.add_message(req, constants.ERROR, 'Usuário já existe com esse email')
                return redirect('/jobs/perfil')
            
            req.user.username = username
            req.user.email = email
            req.user.first_name = first_name
            req.user.last_name = last_name
            req.user.save()
            
            messages.add_message(req, constants.SUCCESS, 'Dados alterados com sucesso')
            return redirect('/jobs/perfil')
        except:
            messages.add_message(req, constants.ERROR, 'Erro interno do sistema')
            return redirect('/jobs/perfil')
                
        
    

def enviar_projeto(req):
    try:
        arquivo = req.FILES.get('file')
        id_job = req.POST.get('id')
        
        job = Jobs.objects.get(id=id_job)
        
        job.arquivo_final = arquivo
        job.status = 'AA'
        job.save()

        messages.add_message(req, constants.SUCCESS, 'Projeto salvo com sucesso')        
        return redirect('/jobs/perfil/')
    except:
        messages.add_message(req, constants.ERROR, 'Erro interno do sistema')
        return redirect('/jobs/perfil/')
        







