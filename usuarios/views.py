from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from controle.forms import Userform, SetPasswordForm
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from controle.models import ControleFinanceiro

# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('login')

def login(request):
    if User.objects.filter(username=request.user).exists():
        return HttpResponse("Usuário {} já está logado.<br>Retorne a página anterior!".format(request.user))
    if request.method=='POST':
        email = request.POST['email']
        senha= request.POST['password']
        if email == "" or senha == "":
            print("Os campos email e senha não podem estar vazios!")
            return redirect('login')
        # Aqui estamos verificando se o usuário já existe
        if User.objects.filter(email=email).exists():
            # Dentre os campos do usuário estamos trazendo apenas a 'username', junto ao parâmetro 'flat=True'
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('Login bem sucedido')
                return redirect('index')
    return render(request, 'login.html')

@login_required(login_url='/usuario/login')
def editar_perfil(request):
    if request.method=='POST':
        username = request.POST['nome']
        email = request.POST['email']
        if campo_vazio(username):
            messages.error(request,'O campo nome completo não pode ficar em branco')
            return redirect('editar_perfil')
        if campo_vazio(email):
            messages.error(request,'O campo email não pode ficar em branco')
            return redirect('editar_perfil')
        #Atualizando os dados do usuário
        User.objects.filter(id=request.user.id).update(username=username,email=email)
        messages.success(request, "Cadastro realizado com sucesso!")
        return redirect('index')
    else:
        return render(request, 'editar_perfil.html')

def novo_usuario(request):
    if request.user.is_authenticated:
        return redirect("editar_perfil")
    if request.method=='POST':
        username = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']
        if campo_vazio(username) or campo_vazio(email):
            messages.error(request,'Os campos nome e email não podem ficar em branco')
            return redirect('novo_usuario')
        if senhas_nao_iguais(senha, senha2):
            messages.error(request, 'As senhas não são iguais')
            print('As senhas não conferem')
            return redirect('novo_usuario')
        if usuario_existe(email) or usuario_existe(username):
            messages.error(request,'Usuário ou Email já cadastrado')
            return redirect('novo_usuario')     
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        print('Usuário cadastrado com sucesso!')
        messages.success(request, "Cadastro realizado com sucesso!")
        return redirect('login')
    else:
        return render(request, 'novo_usuario.html')

@login_required(login_url='/usuario/login')
def alterar_senha(request):
    user=request.user
    if request.method=='POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.error(request, 'Senha alterada com sucesso!')
            return redirect('index')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    form = SetPasswordForm(user)
    return render(request, 'alterar_senha.html', {'form':form})

def campo_vazio(campo):
    return not campo.strip()

def senhas_nao_iguais(senha, senha2):
    return senha != senha2

def usuario_existe(parametro):
    return User.objects.filter(parametro=parametro).exists()