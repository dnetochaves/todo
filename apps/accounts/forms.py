from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

class UserForm(ModelForm):
    class meta:
        model = User
        fields = ['first_name', 'email', 'password']

