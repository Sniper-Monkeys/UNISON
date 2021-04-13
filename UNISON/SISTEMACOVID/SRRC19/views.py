from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db import IntegrityError
from UNISON.SISTEMACOVID.SRRC19.models import *

# Create your views here.

def contactar(request):

    if request.method == "POST":
        asunto = "¡Persona en Estado de Riesgo!"
        mensaje =  "La(s) persona(s): " + request.POST["txtMensaje"] + " está(n) en estado de riesgo nivel MAXIMO"
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["martinxf22@gmail.com"] #AGREGAR OTRO CORREO ELECTRONICO
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
        return render(request,"contactoExitoso.html")
    alumnos = Alumno.objects.all()
    return render(request, "FormularioContacto.html", {"alumnos": alumnos})

def index(request):
    return render(request, "index.html")

def ingresar(request):
    if request.method == "POST":
        inicioexitoso = authenticate(request, username=request.POST.get('usuario'), password=request.POST.get('contrena'))
        if inicioexitoso is None:
            return render(request, 'index.html', {'form': AuthenticationForm(), 'error': 'El Usuario o la Contraseña son incorrectos'})
        else:
            login(request, inicioexitoso)
            return redirect('inicio')
    else:
        return render(request, 'index.html', {'form': AuthenticationForm()})

def inicio(request):
    return render(request, 'inicio.html')
