from django.contrib import admin
from django.urls import path, include
from cadastro.views import cadastrar_locacao, home, sucesso, livros, contato, filtro_livros_locados, confirmacao_locacao


urlpatterns = [
    path('', home, name='home'),
    path('locacao/', cadastrar_locacao, name='locacao'),
    path('sucesso/', sucesso, name='sucesso'),
    path('livros/', livros, name='livros'),
    path('contato/', contato, name='contato'),
    path('filtro/', filtro_livros_locados, name='filtro'),
    path('confirmacao/<int:livro_id>/', confirmacao_locacao, name='confirmacao_locacao'),
]