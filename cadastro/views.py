from django.shortcuts import render, redirect
from django.db import transaction
from .forms import LocacaoForm
from .models import Livro, Locacao
from django.shortcuts import get_object_or_404

def home(request):
    return render(request, 'index.html')

def cadastrar_locacao(request):
    if request.method == 'POST':
        form = LocacaoForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                locacao = form.save(commit=False)

                livro = locacao.livro
                livro.status = 'L'
                livro.save()

                locacao.save()

            return redirect('sucesso')
    else:
        form = LocacaoForm()

    return render(request, 'locacao.html', {'form': form})

def sucesso(request):
    return render(request, 'sucesso.html')

from django.shortcuts import render
from .models import Livro

def livros(request):
    livros_disponiveis = Livro.objects.filter(status='D')
    livros_locados = Livro.objects.filter(status='L')

    return render(request, 'livros.html', {
        'livros_disponiveis': livros_disponiveis,
        'livros_locados': livros_locados
    })


def contato(request):
    return render(request, 'contato.html')

from .forms import FiltroLivroForm

def filtro_livros_locados(request):
    form = FiltroLivroForm(request.GET or None)

    livros = Livro.objects.filter(status='L')

    if form.is_valid():
        area = form.cleaned_data.get('area')
        autor = form.cleaned_data.get('autor')

        if area:
            livros = livros.filter(area__icontains=area)

        if autor:
            livros = livros.filter(autor__icontains=autor)

    context = {
        'form': form,
        'livros': livros
    }

    return render(request, 'filtro.html', context)

def confirmacao_locacao(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)

    locacao = get_object_or_404(
        Locacao,
        livro=livro
    )

    return render(request, 'confirmacao.html', {
        'locacao': locacao
    })