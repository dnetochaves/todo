from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import UserForm, UserProfileForm, UserFormChangeInformation
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth import update_session_auth_hash


# Create your views here.
@login_required(login_url='/accounts/user_login')
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
            messages.success(request, 'Usuário salvo com sucesso !!')
    form = UserForm()
    context['form'] = form
    return render(request, template_name, context)



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

@login_required(login_url='/accounts/user_login')
def user_logout(request):
    logout(request)
    return redirect('accounts:user_login')

@login_required(login_url='/accounts/user_login')
def password_change(request):
    template_name = 'accounts/password_change.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
        else:
            messages.warning(request, 'Deu merda')
    form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)


def add_user_profile(request):
    template_name = 'accounts/add_user_profile.html'
    context = {}
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            messages.success(request, 'Perfil adicionada com sucesso !!')
    form = UserProfileForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/accounts/user_login')
def list_user_profile(request):
    template_name = 'accounts/list_user_profile.html'
    context = {}
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = None
    context['profile'] = profile
    return render(request, template_name, context)

@login_required(login_url='/accounts/user_login')
def change_user_profile(request, username):
    template_name = 'accounts/add_user_profile.html'
    context = {}
    profile = UserProfile.objects.get(user__username=username)
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso!!')
    form = UserProfileForm(instance=profile)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/accounts/user_login')
def change_user_information(request):
    template_name = 'accounts/change_user_information.html'
    context = {}
    user = User.objects.get(username=f_username)
    if request.method == 'POST':
        form = UserFormChangeInformation(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Informações atualizadoas com sucesso!!')
    form = UserFormChangeInformation(instance=user)
    context['form'] = form
    return render(request, template_name, context)
   
   
