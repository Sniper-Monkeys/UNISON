from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
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
