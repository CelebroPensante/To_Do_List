from django.shortcuts import render, redirect
from app.models import Tasks

# Create your views here.
def home(request):
    tasks = Tasks.objects.all().order_by('-priority_task', 'prazo_task') #aqui estamos pegando todas as tarefas do banco de dados e ordenando por prioridade e prazo
    return render(request, 'home.html', {'tasks': tasks})

def add(request):
    if request.method == 'POST': #se o método for POST, então vamos adicionar a tarefa
        add_task = Tasks()
        add_task.title_task = request.POST.get('titulo')
        add_task.description_task = request.POST.get('descricao')
        add_task.complete_task = request.POST.get('completada') == 'on'
        add_task.prazo_task = request.POST.get('data')
        add_task.priority_task = request.POST.get('prioridade')
        add_task.save()
        
        return redirect('home')
    else: #se o método for GET, então vamos renderizar a página de adicionar
        return render(request, 'add.html')

def update_task(request, task_id):
    task = Tasks.objects.get(id_task=task_id) #aqui estamos pegando a tarefa que queremos atualizar
    task.complete_task = not task.complete_task 
    task.save()
    return redirect('home')

def delete_task(request, task_id): #aqui estamos deletando a tarefa
    task = Tasks.objects.get(id_task=task_id) 
    task.delete()
    return redirect('home')