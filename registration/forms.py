from django import forms
from django.contrib.auth.models import User
from .models import User

class UserForm(forms.ModelForm):
    email = forms.EmailField(widget = forms.EmailInput())
    passwd = forms.CharField(widget = forms.PasswordInput())

    class Meta:
        model = User
        fields = ('email', 'passwd')
