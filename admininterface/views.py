from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.forms import formset_factory

from . import jsonapi, forms

def index(request):
    context = {'title': 'index', 'nbar': 'home',}
    return render(request, 'admininterface/index.html', context)


def logs(request):
    context = {'title': 'logs', 'nbar': 'logs',}
    return render(request, 'admininterface/logs.html', context)


def statustest(request):
    context = {
        'title': 'logs',
        'nbar': 'status',
    }
    return render(request, 'admininterface/statustest.html', context)


def settings(request):
    context = {'title':'Settings', 'nbar': 'settings',}

    if( not request.user.is_authenticated ):
        return redirect('login')

    SabNZBDFormSet = formset_factory(forms.SabConfigForm)
    SonarrFormSet = formset_factory(forms.SonarrConfigForm)
    CouchPotatoFormSet = formset_factory(forms.CouchPotatoConfigForm)
    if( request.method == 'POST'):
        sabnzbdformset = SabNZBDFormSet(request.POST, request.FILES, prefix='sabnzbd')
        sonarrformset = SonarrFormSet(request.POST, request.FILES, prefix='sonarr')
        couchpotatoformset = CouchPotatoFormSet(request.POST, request.FILES, prefix='couchpotato')
        if( sabnzbdformset.is_valid() and sonarrformset.is_valid() and couchpotatoformset.is_valid() ):
            pass
    else:
        context['sabnzbdform'] = SabNZBDFormSet(prefix='sabnzbd')
        context['sonarrform'] = SonarrFormSet(prefix='sabnzbd')
        context['couchpotatoform'] = CouchPotatoFormSet(prefix='sabnzbd')
    return render(request, 'admininterface/settings.html', context)


def loginView(request):
    context = {
        'title': 'Login',
        'nbar': 'login',
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
                context['status'] = 'Error'
                context['message'] = 'Wrong username or password'
    else:
        form = forms.Login()
    context['form'] = form
    return render(request, 'admininterface/login.html', context)


def logoutView(request):
    logout(request)
    context = {
        'title': 'logout',
        'nbar': 'login',
        'message': 'successfully logged out',
    }
    return render(request, 'admininterface/success.html', context)


def api(request):
    if(request.method == 'GET'):
        return JsonResponse(jsonapi.sabAPI('http://sabnzbd.vestern.se:8080',
                                           'unknown', request.GET))
    return JsonResponse({'status': 'failed'})
