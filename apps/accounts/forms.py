from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import UserProfile


class UserForm(forms.ModelForm):
    class meta:
        model = User
        fields = ['first_name', 'email', 'password']

class UserFormChangeInformation(forms.ModelForm):
    class meta:
        model = User
        fields = ['first_name', 'Last_name', 'email']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['photo', 'cell_phone']