from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'homeapp/home.html')

def entrar(request):
    return render(request, 'homeapp/entrar.html')

def sobre(request):
    return render(request, 'homeapp/sobre.html')

def ajuda(request):
    return render(request, 'homeapp/ajuda.html')

def aluno(request):
    return render(request, 'homeapp/aluno.html')

def base(request):
    return render(request, 'homeapp/base.html')

def dashboard(request):
    return render(request, 'homeapp/dashboard.html')

def cadastro(request):
    return render(request, 'homeapp/cadastro.html')