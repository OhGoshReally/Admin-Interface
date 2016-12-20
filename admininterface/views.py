from django.shortcuts import render


def index(request):
    context = {
        'title': 'index',
        }
    return render(request, 'admininterface/index.html', context)


def logs(request):
    context = {
    'title': 'logs',
    }
    return render(request, 'admininterface/logs.html', context)


def statustest(request):
    context = {
        'title': 'logs',
    }
    return render(request, 'admininterface/statustest.html', context)
