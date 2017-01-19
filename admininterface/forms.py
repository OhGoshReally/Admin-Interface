from django import forms
from .models import SabConfig, User


class Login(forms.Form):
    username = forms.CharField(label='Username')
    username.widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username or email'})
    password = forms.CharField(label='Password')
    password.widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'})
    rememberMe = forms.BooleanField(required=False)


class SabConfigForm(forms.ModelForm):
    class Meta:
        model = SabConfig
        fields = ['url', 'apikey', 'visible']


class SonarrConfigForm(forms.ModelForm):
    class Meta:
        model = SabConfig
        fields = ['url', 'apikey', 'visible']


class CouchPotatoConfigForm(forms.ModelForm):
    class Meta:
        model = SabConfig
        fields = ['url', 'apikey', 'visible']
