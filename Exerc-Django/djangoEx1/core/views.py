from django.shortcuts import render, get_object_or_404
from .models import Produtos
from django.http import HttpResponse
from django.template import loader


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
    # prod = Produtos.objects.get(id=pk)
    prod = get_object_or_404(Produtos, id=pk)
    context = {
        'produto': prod
    }
    return render(request, "produto.html", context)


def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=UTF-8', status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=UTF-8', status=500)
