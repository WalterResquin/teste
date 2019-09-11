from django.urls import path

from paginas.views import paginaInicioView, paginaAboutView, paginaProdutoView, paginaHomeView

urlpatterns = [
    path('', paginaInicioView, name='inicio'),
    path('about', paginaAboutView, name='about'),
    path('produto', paginaProdutoView, name='produto'),
    path('home', paginaHomeView, name='home')
]