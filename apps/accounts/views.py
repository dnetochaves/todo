from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserForm
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

# Create your views here.
@login_required(login_url='/accounts/user_login/')
def begin(request):
    return render(request, 'accounts/begin.html', {})

#Função com probleba 
'''
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
'''

class RegisterUser(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts/begin')
    template_name = 'accounts/add_user.html'


def user_login(request):
    template_name = 'accounts/user_login.html'
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET.get('next', '/'))
        else:
            messages.error(request, 'Deu merda !!')
    return render(request, template_name, {})

def user_logout(request):
    logout(request)
    return redirect('accounts:user_login')

        
def password_change(request):
    template_name = 'accounts/password_change.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
    else:
        messages.warning(request, 'Deu merda na alteração da senha')  
    form = PasswordChangeForm(user=request.user)  
    context['form'] = form
    return render(request, template_name, context)