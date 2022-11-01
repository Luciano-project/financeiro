from django.shortcuts import render, redirect, get_object_or_404
from .models import ControleFinanceiro
from django.contrib.auth.decorators import login_required
from .forms import ItemForm

def index(request):
    if request.user.is_authenticated:
        id_usuario = request.user.id
        contabilidade = ControleFinanceiro.objects.filter(usuario=id_usuario)
        entradas = contabilidade.filter(receita_despesa=1).values_list('valor')
        saidas = contabilidade.filter(receita_despesa=2).values_list('valor')
        saldo = soma_valores(entradas)-soma_valores(saidas)
        dados = {
            'contabilidade': contabilidade,
            'saldo': saldo,
        }
        return render(request, 'index.html', dados)
    else:      
        return redirect('login')

def soma_valores(lista):
    total=0
    for item in lista:
        total+=item[0]
    return total

@login_required(login_url='/usuario/login')
def registro_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():      
        itens = form.save(commit=False)
        id_user= request.user
        itens.usuario = id_user
        form.save()
        return redirect('index')
    return render(request,'cadastro.html',{'form':form})

@login_required(login_url='/usuario/login')
def editar_item(request,id):
    id_usuario = request.user.id
    contabilidade = ControleFinanceiro.objects.filter(usuario=id_usuario)
    item = contabilidade.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request,'cadastro.html',{'form':form},{'item':item})

@login_required(login_url='/usuario/login')
def deleta_item(request,item_id):
    usuario_logado = request.user.id
    itens_usuario_logado=ControleFinanceiro.objects.filter(usuario=usuario_logado)
    receita=get_object_or_404(itens_usuario_logado, pk=item_id)
    receita.delete()
    return redirect('index')
