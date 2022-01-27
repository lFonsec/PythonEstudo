from django.shortcuts import render
from .models import Produtos


def index(request):
    produtos = Produtos.objects.all()
    context = {
        'teste': 'this is a ?',
        'produtos': produtos
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, pk):
    prod = Produtos.objects.get(id=pk)
    context = {
        'produto': prod
    }
    return render(request, "produto.html", context)
