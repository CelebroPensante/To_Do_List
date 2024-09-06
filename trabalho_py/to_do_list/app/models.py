from django.db import models

# Create your models here.
class Tasks(models.Model):
    id_task = models.AutoField(primary_key=True) #aqui é a chave primária
    title_task = models.CharField(max_length=200) #aqui é o título da tarefa
    description_task = models.TextField() #aqui é o título da tarefa
    complete_task = models.BooleanField(default=False) #aqui é o campo que indica se a tarefa está completa ou não
    prazo_task = models.DateTimeField()  #aqui é o campo que indica a data de prazo da tarefa
    priority_task = models.CharField(max_length=10, choices=[('3', 'Alta'), ('2', 'Média'), ('1', 'Baixa')], default='1') #aqu é o campo que indica a prioridade da tarefa