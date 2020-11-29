from django.shortcuts import render, get_object_or_404, redirect
from .forms import CategoryForm, TaskForm
from django.contrib import messages
from .models import Category, Tasks
# Create your views here.


def begin(request):
    return render(request, 'tasks/add_category.html', {})


def add_category(request):
    template_name = 'tasks/add_category.html'
    context = {}
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.owner = request.user
            f.save()
            messages.success(request, 'Categoria adicionada com sucesso !!')
    form = CategoryForm()
    context['form'] = form
    return render(request, template_name, context)


def list_category(request):
    template_name = 'tasks/list_categories.html'
    categories = Category.objects.filter(owner=request.user)
    context = {
        'categories': categories
    }
    return render(request, template_name, context)


def edit_category(request, id_category):
    template_name = 'tasks/add_category.html'
    context = {}
    category = get_object_or_404(Category, id=id_category, owner=request.user)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('tasks:list_category')
    form = CategoryForm(instance=category)
    context['form'] = form
    return render(request, template_name, context)

def delete_category(request, id_category):
    category = Category.objects.get(id=id_category)
    if category.owner == request.user:
        category.delete()
    else:
        messages.error(request, 'Você não tem permissão para excluir essa categoria')
        return redirect('tasks:list_category')
    return redirect('tasks:list_category')

def add_task(request):
    template_name = 'tasks/add_task.html'
    context = {}
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.owner = request.user
            f.save()
            form.save_m2m()
            messages.success(request, 'Tarefa adicionada com sucesso !!')
            return redirect('tasks:list_task')
           
    form = TaskForm()
    context['form'] = form
    return render(request, template_name, context)


def list_task(request):
    template_name = 'tasks/list_task.html'
    tasks = Tasks.objects.filter(owner=request.user).exclude(status='CD')
    context = {
        'tasks': tasks
    }
    return render(request, template_name, context)


def edit_task(request, id_task):
    template_name = 'tasks/add_task.html'
    context = {}
    task = get_object_or_404(Tasks, id=id_task, owner=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks:list_task')
    form = TaskForm(instance=task)
    context['form'] = form
    return render(request, template_name, context)

def delete_task(request, id_task):
    task = Tasks.objects.get(id=id_task)
    if task.owner == request.user:
        task.delete()
    else:
        messages.error(request, 'Você não tem permissão para excluir essa tarefa')
        return redirect('tasks:list_task')
    return redirect('tasks:list_task')