from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import AlunoForm
from .models import Aluno


# Create your views here.
def index(request):
    alunos = Aluno.objects.all()
    context = alunos
    return render(request, 'index.html', {'alunos': context})

def detalhes(request, id):
    aluno = Aluno.objects.get(pk=id)
    return render(request, 'details.html', {'aluno': aluno})

def editar(request, id):
    aluno = Aluno.objects.get(pk=id)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(index))
        else:
            return render(request, 'edit.html', {'form': form})
        
    else:
        form = AlunoForm(instance=aluno)
        return render(request, 'edit.html', {'form': form})


def criar(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            aluno = Aluno()
            aluno.nome = form.cleaned_data['nome']
            aluno.idade = form.cleaned_data['idade']
            aluno.endereco = form.cleaned_data['endereco']
            aluno.email = form.cleaned_data['email']
            aluno.data_de_nascimento = form.cleaned_data['data_de_nascimento']
            aluno.cidade = form.cleaned_data['cidade']
            aluno.curso = form.cleaned_data['curso']
            aluno.save()
            return HttpResponseRedirect(reverse(index))
        
        else:
            return render(request, 'create.html', {'form': form})
        
    else:
        form = AlunoForm()
        return render(request, 'create.html', {'form': form})
    
def deletar(request, id):
    aluno = Aluno.objects.get(pk=id)
    aluno.delete()
    return HttpResponseRedirect(reverse(index))