from django.urls import path

from .views import ProdutoListView, ProdutoDetailView
from paginas.views import paginaInicioView, paginaAboutView, paginaProdutoView, paginaHomeView, paginaContatoView, paginaCadastroView, paginaLoginView

urlpatterns = [
    path('', paginaInicioView, name='inicio'),
    path('about', paginaAboutView, name='about'),
    path('contato', paginaContatoView, name='contato'),
    path('cadastro', paginaCadastroView, name='cadastro'),
    path('login', paginaLoginView, name='login'),
    #path('produto', paginaProdutoView, name='produto'),
    #path('home', paginaHomeView, name='home'),
    path('home', ProdutoListView.as_view(), name='home'),
    path('produto/<int:pk>', ProdutoDetailView.as_view(), name='produto_detail'),
]