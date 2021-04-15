from django.db import models

#python manage.py createmigrate <- Para almacenar modelo de base de datos
#python manage.py createsuperuser <- Para agregar un super usuario
#python manage.py migrate <- Para actualizar modelo de base de datos
#NO ABRIR UNIVERSIDAD.DB

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class User(AbstractUser):
    ApellidoPaterno = models.CharField(max_length=35)
    ApellidoMaterno = models.CharField(max_length=35)
    Matricula = models.CharField(max_length=35)
# Modelos de la base de datos.
