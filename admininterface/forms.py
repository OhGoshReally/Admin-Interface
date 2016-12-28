from django import forms

class Login(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class SabConfig(forms.Form):
    url = forms.CharField(label='URL')
    apikey = forms.CharField(label='API Key')
