from django import forms
from .models import SabConfig, User


class Login(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class SabConfigForm(forms.ModelForm):
    class Meta:
        Model = SabConfig
        fields = ['url', 'apikey', 'visible']
