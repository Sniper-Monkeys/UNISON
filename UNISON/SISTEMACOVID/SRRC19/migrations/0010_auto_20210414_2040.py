# Generated by Django 3.1.7 on 2021-04-15 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SRRC19', '0009_user_matricula'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='ApellidoMaterno',
        ),
        migrations.RemoveField(
            model_name='user',
            name='ApellidoPaterno',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Matricula',
        ),
        migrations.AddField(
            model_name='user',
            name='matricula',
            field=models.IntegerField(default=123, max_length=10),
            preserve_default=False,
        ),
    ]