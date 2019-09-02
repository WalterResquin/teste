from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def paginaInicioView(resquest):
    return HttpResponse('<h1 style="font-size:24px;color:green">AC 02 Finalizada! </br> Bem vindo ao curso de E-commerce!</h1>')