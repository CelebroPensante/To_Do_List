# Generated by Django 5.1.1 on 2024-09-06 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id_task', models.AutoField(primary_key=True, serialize=False)),
                ('title_task', models.CharField(max_length=200)),
                ('complete_task', models.TextField()),
                ('created_task', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
