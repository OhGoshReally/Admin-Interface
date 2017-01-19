from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages

from . import jsonapi, forms

def index(request):
    context = {'title': 'index',}
    return render(request, 'admininterface/index.html', context)


def logs(request):
    context = {'title': 'logs',}
    return render(request, 'admininterface/logs.html', context)


def statustest(request):
    context = {
        'title': 'logs',
    }
    return render(request, 'admininterface/statustest.html', context)


def settings(request):
    if(not request.user.is_authenticated()):
        return redirect('login')
    else:
        if(request.method == 'POST'):
            form = forms.SabConfig(request.POST)
            if(form.is_valid()):
                url = form.cleaned_data['url']
                key = form.cleaned_data['apikey']
                form.save()
        else:
            form = forms.SabConfig
    context = {'title': 'Settings', 'form': form}
    return render(request, 'admininterface/settings.html', context)



def loginView(request):
    context = {
        'title': 'Login',
    }
    if(request.user.is_authenticated()):
        return redirect('index')
    if(request.method == 'POST'):
        form = forms.Login(request.POST)
        if (form.is_valid()):
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if (user != None):
                login(request, user)
                context['message'] = 'Successfully logged in!'
                context['redirect'] = 'index'
                return render(request, 'admininterface/success.html', context)
    else:
        form = forms.Login()
    context['form'] = form
    return render(request, 'admininterface/login.html', context)


def logoutView(request):
    logout(request)
    context = {
        'title': 'logout',
        'message': 'successfully logged out',
    }
    return render(request, 'admininterface/success.html', context)


def api(request):
    if(request.method == 'GET'):
        return JsonResponse(jsonapi.sabAPI('http://sabnzbd.vestern.se:8080',
                                           'unknown', request.GET))
    return JsonResponse({'status': 'failed'})
