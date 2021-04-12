# Generated by Django 3.1.7 on 2021-04-12 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ApellidoPaterno', models.CharField(max_length=35)),
                ('ApellidoMaterno', models.CharField(max_length=35)),
                ('Nombres', models.CharField(max_length=35)),
                ('Matricula', models.CharField(max_length=8)),
                ('DiaDeIngreso', models.CharField(max_length=5)),
                ('Sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='M', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Nombre_Docente', models.CharField(max_length=50)),
                ('Creditos', models.PositiveSmallIntegerField()),
                ('Disponible', models.BooleanField(default=True)),
            ],
        ),
    ]
