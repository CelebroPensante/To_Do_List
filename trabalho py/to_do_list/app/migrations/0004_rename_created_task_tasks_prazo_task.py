# Generated by Django 5.1.1 on 2024-09-06 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_tasks_priority_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='created_task',
            new_name='prazo_task',
        ),
    ]
