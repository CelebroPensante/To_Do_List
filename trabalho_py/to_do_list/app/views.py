from django.shortcuts import render, redirect
from app.models import Tasks
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

#def home pronta até q enfim bagulho é o seguinte se o usuário for superuser ele pode ver todas as tarefas se não ele só pode ver as tarefas dele
#todas as linhas comentadas pra facilitar o entendimento
@login_required
def home(request):
    # Obtém o filtro de status da solicitação GET
    status_filter = request.GET.get('status')
    # Obtém o filtro de usuário da solicitação GET
    user_filter = request.GET.get('user')
    
    # Verifica se o usuário logado é um superusuário (administrador)
    if request.user.is_superuser:
        # Se for administrador, obtém todas as tarefas
        tasks = Tasks.objects.all()
        # Obtém todos os usuários para o filtro de usuário
        users = User.objects.all()
        # Aplica o filtro de usuário, se fornecido
        if user_filter:
            tasks = tasks.filter(user_id=user_filter)
    else:
        # Se não for administrador, obtém apenas as tarefas do usuário logado
        tasks = Tasks.objects.filter(user=request.user)
    
    # Aplica o filtro de status, se fornecido
    if status_filter:
        tasks = tasks.filter(complete_task=status_filter)
    
    # Ordena as tarefas por prioridade (decrescente) e prazo (crescente)
    tasks = tasks.order_by('-priority_task', 'prazo_task')
    
    # Cria o contexto a ser passado para o template
    context = {
        'tasks': tasks,
    }
    
    # Se o usuário for administrador, adiciona a lista de usuários ao contexto
    if request.user.is_superuser:
        context['users'] = users
    
    # Renderiza o template 'home.html' com o contexto
    return render(request, 'home.html', context)


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
    
def edit_task(request, task_id): #adicionar tarefa
    add_task = Tasks.objects.get(id_task=task_id, user=request.user)
    if request.method == 'POST':
        add_task.title_task = request.POST.get('titulo')
        add_task.description_task = request.POST.get('descricao')
        add_task.complete_task = request.POST.get('status')
        add_task.prazo_task = request.POST.get('data')
        add_task.priority_task = request.POST.get('prioridade')
        add_task.user = request.user  # Associe a tarefa ao usuário logado
        add_task.save()
        
        return redirect('home')
    else:
        return render(request, 'editar.html')

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