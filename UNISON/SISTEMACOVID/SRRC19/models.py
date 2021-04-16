from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import pre_save
from django_model_changes import ChangesMixin
from django.dispatch import receiver
from django.shortcuts import render, redirect
# python manage.py createmigrate <- Para almacenar modelo de base de datos
# python manage.py createsuperuser <- Para agregar un super usuario
# python manage.py migrate <- Para actualizar modelo de base de datos
# NO ABRIR UNIVERSIDAD.DB

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class User(AbstractUser):
    matricula = models.CharField(max_length=50, default='xxxxxxxx')
    OCUPACION = (('A', 'Alumno'), ('D', 'Docente'), ('P', 'Personal Administrativo'))
    ocupacion = models.CharField(max_length=1, choices=OCUPACION, default='A')
    RIESGO = (('R', 'Rojo'), ('M', 'Naranja'), ('A', 'Amarillo'), ('V', 'Verde'))
    riesgo = models.CharField(max_length=1, choices=RIESGO, default='V')
    CORREOMANDADO = (('S', 'SI'),('N', 'NO'))
    CorreoMandado = models.CharField(max_length=1, choices=CORREOMANDADO, default='N')
