from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import UserForm
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy

# Create your views here.
def begin(request):
    return render(request, 'accounts/begin.html', {})

def add_user(request):
    template_name = 'accounts/add_user.html'
    context = {}
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.set_password(f.password)
            f.save()
    form = UserForm()
    context['form'] = form
    return render(request, template_name, context)

class RegisterUser(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('127.0.0.1:8000/')
    template_name = 'accounts/add_user.html'

        