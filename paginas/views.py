from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import Produto

# Create your views here.

def paginaInicioView(req):
    if req.method == 'GET':
        print(req.GET)
        return HttpResponse('<h1 style="font-size:24px;color:green">AC 02 Finalizada! </br> Bem vindo ao curso de E-commerce!</h1>')

def paginaAboutView(req):
    #return HttpResponse('<h1> Página com informação sobre o site.</h1>')
    return render(req, 'paginas/about.html', {})

def paginaProdutoView(req):
    return HttpResponse('<h1> Página Produto.</h1>')

def paginaHomeView(req):
    return render(req, 'paginas/home.html', {})
    #return HttpResponse('<h1> Página Produto.</h1>')

def paginaContatoView(req):
    return render(req, 'paginas/contato.html', {})

def paginaCadastroView(req):
    return render(req, 'paginas/cadastro.html', {})

def paginaLoginView(req):
    return render(req, 'paginas/login.html', {})



class ProdutoListView(ListView):
    model = Produto
    template_name = "paginas/home.html"

class ProdutoDetailView(DetailView):
    model = Produto
    template_name = "paginas/produto_detail.html"
