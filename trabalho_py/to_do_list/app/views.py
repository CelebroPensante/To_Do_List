from django.shortcuts import render, redirect
from app.models import Tasks
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm

def register(request): #registrar novo usuário
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def home(request): #página inicial
    tasks = Tasks.objects.filter(user=request.user).order_by('-priority_task', 'prazo_task')
    return render(request, 'home.html', {'tasks': tasks})

@login_required
def add(request): #adicionar tarefa
    if request.method == 'POST':
        add_task = Tasks()
        add_task.title_task = request.POST.get('titulo')
        add_task.description_task = request.POST.get('descricao')
        add_task.complete_task = request.POST.get('status')
        add_task.prazo_task = request.POST.get('data')
        add_task.priority_task = request.POST.get('prioridade')
        add_task.user = request.user  # Associe a tarefa ao usuário logado
        add_task.save()
        
        return redirect('home')
    else:
        return render(request, 'add.html')

@login_required
def update_task(request, task_id): #atualizar tarefa
    task = Tasks.objects.get(id_task=task_id, user=request.user)  # Filtre pela tarefa e pelo usuário
    task.complete_task = not task.complete_task 
    task.save()
    return redirect('home')

@login_required 
def delete_task(request, task_id): #deletar tarefa
    task = Tasks.objects.get(id_task=task_id, user=request.user)  # Filtre pela tarefa e pelo usuário
    task.delete()
    return redirect('home')

def logout(request): #deslogar da conta
    auth_logout(request)
    return redirect('login')