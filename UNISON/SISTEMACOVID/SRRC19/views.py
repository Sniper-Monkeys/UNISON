from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from UNISON.SISTEMACOVID.SRRC19.models import *
from django.contrib import messages  # import messages


# Create your views here.

def contactar(request):
    if request.method == "POST":
        asunto = "¡Persona en Estado de Riesgo!"
        mensaje = "La(s) persona(s): " + request.POST["txtMensaje"] + " está(n) en estado de riesgo"
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["martinxf22@gmail.com"]  # AGREGAR OTRO CORREO ELECTRONICO
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
        messages.success(request, "Mensaje enviado correctamente.")
    alumnos = Alumno.objects.all()
    return render(request, "index.html", {"alumnos": alumnos})


def ingresar(request):
    if request.method == "POST":
        inicioexitoso = authenticate(request, username=request.POST.get('usuario'),
                                     password=request.POST.get('contrasena'))
        if inicioexitoso is None:
            return render(request, 'login.html',
                          {'form': AuthenticationForm(), 'error': 'El Usuario o la contraseña son incorrectos... '})
        else:
            login(request, inicioexitoso)
            return redirect('contacto')
    else:
        return render(request, 'login.html', {'form': AuthenticationForm()})

def salida(request):
    if request.method == "POST":
        logout(request)
        return redirect('ingresarpagina')
