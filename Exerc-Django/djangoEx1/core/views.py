from django.shortcuts import render


def index(request):
    context = {
        'teste': 'this is a ?'
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')
