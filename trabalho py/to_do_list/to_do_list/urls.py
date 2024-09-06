"""
URL configuration for to_do_list project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), #esta é a rota principal
    path('add', views.add, name='add'), #esta é a rota para adicionar uma tarefa
    path('update_task/<int:task_id>/', views.update_task, name='update_task'), #esta é a rota para atualizar uma tarefa
    path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'), #esta é a rota para deletar uma tarefa
]
