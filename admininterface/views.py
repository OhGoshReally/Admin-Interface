from django.shortcuts import render
from django.http import JsonResponse

from . import jsonapi

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


def api(request):
    if(request.method == 'GET'):
        return JsonResponse(jsonapi.sabAPI('http://sabnzbd.vestern.se:8080',
                                           'unknown', request.GET))
    return HttpResponse("Something`s fucky")
