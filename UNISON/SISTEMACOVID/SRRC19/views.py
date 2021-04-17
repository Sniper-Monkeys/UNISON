from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.template.loader import render_to_string
from UNISON.SISTEMACOVID.SRRC19.models import *
from django.contrib import messages  # import messages


# Create your views here.

def contactar(request):  # Queda obsolote por ahora, lo dejo como referencia para los correos
    if request.method == "POST":
        asunto = "¡Persona en Estado de Riesgo!"
        mensaje = "La(s) persona(s): " + request.POST["txtMensaje"] + " está(n) en estado de riesgo"
        email_desde = settings.EMAIL_HOST_User
        email_para = ["martinxf22@gmail.com"]  # AGREGAR OTRO CORREO ELECTRONICO
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
        messages.success(request, "Mensaje enviado correctamente.")
    alumnos = User.objects.all()
    return render(request, "index.html", {"alumnos": alumnos})


def ingresar(request):
    if request.method == "POST":
        print(request.POST.get('usuario'))

        inicioexitoso = authenticate(request, username=request.POST.get('usuario'),
                                     password=request.POST.get('contrasena'))
        if inicioexitoso is None:

            return render(request, 'login.html',
                          {'form': AuthenticationForm(), 'error': 'El Usuario o la contraseña son incorrectos... '})
        else:
            login(request, inicioexitoso)
            return redirect('iniciopagina')
    else:
        return render(request, 'login.html', {'form': AuthenticationForm()})


def inicio(request):

    alumnos = User.objects.all()
    cantidadEstadoDeRiesgo = 0
    for alu in User.objects.all():
        if alu.riesgo == 'R':
            cantidadEstadoDeRiesgo+=1


   # for alu in User.objects.all():
   #     if alu.riesgo == 'R' and alu.CorreoMandado == 'N':
   #         asunto = "¡ESTAS EN ESTADO DE RIESGO!"
   #         mensaje = render_to_string('email_template.html',
    #                                   {'name': alu.get_full_name(),
     #                                   'expediente': alu.matricula}
    #                                   )
     #       email_desde = settings.EMAIL_HOST_USER
      #      email_para = [alu.email]
      #      send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
       #     alu.CorreoMandado = 'S'
        #    alu.save()
         #   messages.success(request, "Mensaje enviado correctamente.")


    return render(request, "index.html", {"alumnos": alumnos})


def perfil(request):
    # t.Matricula = 219205955
    # t.save()
    return render(request, 'perfil.html')


def salida(request):
    if request.method == "POST":
        logout(request)
        return redirect('ingresarpagina')


def Mandar_correo(request):
    t = User.objects.get(username=request.user.username)
    if t.riesgo == 'R':
        asunto = "¡Persona en Estado de Riesgo!"
        mensaje = "La(s) persona(s): " + t.username + " está(n) en estado de riesgo"
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["martinxf22@gmail.com"]  # AGREGAR OTRO CORREO ELECTRONICO
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
        messages.success(request, "Mensaje enviado correctamente.")
    return render(request, 'index.html')


def Realizar_Encuesta(request):
    return render(request, 'encuesta.html')


def Buscar_Alumno(request):
    return render(request, 'buscar.html')


def Perfil_Buscado(request):
    if request.method == 'GET':
        busqueda = request.GET.get('busqueda')
        alumno = User.objects.all().filter(matricula=busqueda)


        return render(request, 'perfil_buscado.html', {'alumno': alumno})



    return render(request, 'perfil_buscado.html')


def Reportar(request):
    return render(request, 'reportar.html')



def Generar_Reporte(request):
    if request.method == 'POST':
        reporte = Reporte.objects.create(matricula_reportado=request.POST.get('matricula'))
        reporte.NoCubrebocas = request.POST.get('respuesta1')
        reporte.GelSanitizante =  request.POST.get('respuesta2')
        reporte.NoRespetarAforo =  request.POST.get('respuesta3')
        reporte.NoRespetarSanaDistancia =  request.POST.get('respuesta4')
        reporte.NoRealizarEncuestaSemanal =  request.POST.get('respuesta5')
        reporte.NoRespetarEstadoDeRiesgo =  request.POST.get('respuesta6')
        reporte.AsistirDiasSeguidos =  request.POST.get('respuesta7')
        reporte.Comentarios = request.POST.get('comment')
        reporte.save()
        messages.success(request,'Se ha mandado el reporte correctamente')
    return redirect('iniciopagina')




