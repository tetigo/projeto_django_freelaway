from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth

# Create your views here.
def cadastro(req):
    if req.user.is_authenticated:
        return redirect('/')
    if req.method == 'GET':
        return render(req, 'cadastro.html', context={})
    if req.method == 'POST':
        username = req.POST.get('username')
        senha = req.POST.get('password')
        confirma_senha = req.POST.get('confirm-password')

        if len(senha.strip()) == 0 or len(confirma_senha.strip()) == 0:
            messages.add_message(req, constants.ERROR, 'Senhas não conferem')
            return redirect('/auth/cadastro')
        
        if not senha == confirma_senha:
            messages.add_message(req, constants.ERROR, 'Senhas não conferem')
            return redirect('/auth/cadastro')
        
        user = User.objects.filter(username=username)
        
        if user.exists():
            messages.add_message(req, constants.ERROR, 'Usuário já existe')
            return redirect('/auth/cadastro')
        
        try:
            user = User.objects.create_user(username=username, password=senha)
            user.save()
            messages.add_message(req, constants.SUCCESS, 'Cadastrado com sucesso')
            return redirect('/auth/login')
        except:
            messages.add_message(req, constants.SUCCESS, 'Erro interno do sistema')
            return redirect('/auth/cadastro')
    

def login(req):
    if req.user.is_authenticated:
        return redirect('/')
    if req.method == 'GET':
        return render(req, 'login.html', context={})
    if req.method == 'POST':
        username = req.POST.get('username')
        senha = req.POST.get('password')
        
        user = auth.authenticate(req, username=username, password=senha)
        
        if not user:
            messages.add_message(req, constants.ERROR, 'Usuário não encontrado')
            return redirect('/auth/login')
        
        auth.login(request=req, user=user)
        return redirect('/jobs/encontrar_jobs/')


def logout(req):
    auth.logout(req)
    return redirect('/auth/login')













