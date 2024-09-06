from django.db import models
from django.contrib.auth.models import User

class Tasks(models.Model):
    id_task = models.AutoField(primary_key=True) #chave primária
    title_task = models.CharField(max_length=200) #título da tarefa
    description_task = models.TextField() #descrição da tarefa
    complete_task = models.BooleanField(default=False) #tarefa completada
    prazo_task = models.DateTimeField()  #prazo da tarefa
    priority_task = models.CharField(max_length=10, choices=[('3', 'Alta'), ('2', 'Média'), ('1', 'Baixa')], default='1') #prioridade da tarefa
    user = models.ForeignKey(User, on_delete=models.CASCADE) #usuário que criou a tarefa