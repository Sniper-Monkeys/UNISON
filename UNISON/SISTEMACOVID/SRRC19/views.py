from django.http import HttpResponseRedirect
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
            usuario = User.objects.get(username=request.POST.get('usuario'))
            if usuario.ocupacion == "A":
                return redirect('inicioApagina')
            elif usuario.ocupacion == "D":
                return redirect('inicioDpagina')
            elif usuario.ocupacion == "P":
                return redirect('inicioPpagina')
            return redirect('ingresarpagina')
    else:
        return render(request, 'login.html', {'form': AuthenticationForm()})


def inicio(request):

    alumnos = User.objects.all()

    # Add the results to the many to many field (notice the *)


    cantidadEstadoDeRiesgo = 0


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


def Inicio_Alumno(request):
    Talum = User.objects.all().filter(ocupacion="A")
    cantidadEstadoDeRiesgo = 0
    for i in Talum:
        if i.riesgo == 'R':
            cantidadEstadoDeRiesgo += 1
    valor = (cantidadEstadoDeRiesgo / len(Talum)) * 100
    promedio = round(valor, 2)

    return render(request, 'inicio_alumno.html',{"promedio": promedio})


def Inicio_Docente(request):
    group = []
    alumnos = []
    cantidadEstadoDeRiesgo = 0

    grupos = Grupos.objects.all()
    for grupo in grupos:
        if grupo.Profesor.Docente == request.user:
            group = grupo

   # group = Grupos.objects.get(Materia='Ingeniería en Software 1')
    #print(group.Profesor.Correo)
    for i in group.users.values():
        alumnos.append(i)
        if i["riesgo"] == "R":
            cantidadEstadoDeRiesgo += 1
    Talum = User.objects.all().filter(ocupacion= "A")
    Triesgo = 0
    for alum in Talum:
        if alum.riesgo == 'R':
            Triesgo+=1

    valor = (Triesgo / len(Talum)) * 100
    promedio = round(valor,2)
    #print(cantidadEstadoDeRiesgo)

    return render(request, 'inicio_docente.html', {"alumnos": alumnos , "contagiados": cantidadEstadoDeRiesgo, "promedio": promedio})


def Inicio_Administrativo(request):
    Talum = User.objects.all().filter(ocupacion= "A")
    cantidadEstadoDeRiesgo = 0
    for i in Talum:
        if i.riesgo == 'R':
            cantidadEstadoDeRiesgo += 1
    valor = (cantidadEstadoDeRiesgo / len(Talum)) * 100
    promedio = round(valor,2)
    promedio2 = 100-promedio
    return render(request, 'inicio_administrativo.html', {"alumnos": Talum , "contagiados": cantidadEstadoDeRiesgo, "promedio": promedio, "promedio2":promedio2})


def perfil(request):
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
        email_para = [User.objects.filter(ocupacion= 'P')]  # AGREGAR OTRO CORREO ELECTRONICO
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
        reportes = Reporte.objects.filter(matricula_reportado=request.GET.get('busqueda'))

        return render(request, 'perfil_buscado.html', {'alumno': alumno,"reporte":reportes})



    return render(request, 'perfil_buscado.html')


def Reportar(request):
    return render(request, 'reportar.html')



def Generar_Reporte(request):
    if request.method == 'POST':
        reporte = Reporte.objects.create(matricula_reportado=request.POST.get('matricula'))

        reporte.hora = datetime.now()
        reporte.NoCubrebocas = request.POST.get('respuesta1')
        reporte.NoRespetarAforo = request.POST.get('respuesta2')
        reporte.NoRespetarSanaDistancia = request.POST.get('respuesta3')
        reporte.NoRealizarEncuestaSemanal = request.POST.get('respuesta4')
        reporte.NoRespetarEstadoDeRiesgo = request.POST.get('respuesta5')
        reporte.Comentarios = request.POST.get('comment')
        reporte.save()
        alumno = User.objects.get(matricula=request.POST.get('matricula'))
        print(request.POST.get('matricula'))
        alumno.puntos += 5

        alumno.save(update_fields=['puntos'])

        messages.success(request, 'Se ha mandado el reporte correctamente')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def Generar_Encuesta(request):
    if request.method == 'POST':
        encuesta = Encuesta.objects.create(matricula_encuestado=request.user.matricula,nombre_encuestado=request.user.get_full_name())

        print(request.user.matricula)
        encuesta.nombre_reportado = request.user.get_full_name()
        encuesta.fecha = datetime.now()

        encuesta.positivoCovid = bool(request.POST.get('respuesta1'))
        encuesta.gripa = request.POST.get('respuesta2')
        encuesta.fiebre = request.POST.get('respuesta3')
        encuesta.tos = request.POST.get('respuesta4')
        encuesta.problemasRespiratorios = request.POST.get('respuesta5')
        encuesta.dolorCabeza = request.POST.get('respuesta6')
        encuesta.dolorMuscular = request.POST.get('respuesta7')
        encuesta.dolorGarganta = request.POST.get('respuesta8')
        encuesta.perdidaOlfato = request.POST.get('respuesta9')
        encuesta.perdidaGusto= request.POST.get('respuesta10')
        encuesta.cansancio = request.POST.get('respuesta11')
        encuesta.PersonasContacto = request.POST.get('respuesta12')


        if not request.POST.get("cardiovascular") is None:
            encuesta.problemaCardiovascular = 1
        if not request.POST.get("asma") is None:
            encuesta.asma = 1
        if not request.POST.get("cancer") is None:
            encuesta.cancer = 1
        if not request.POST.get("diabetes") is None:
            encuesta.diabetes = 1
        if not request.POST.get("bronquitis") is None:
            encuesta.bronquitis = 1
        if not request.POST.get("otro") is None:
            encuesta.otrosProblemas = 1

        if not request.POST.get("cine") is None:
            encuesta.cine = 1
        if not request.POST.get("centro") is None:
            encuesta.centroComercial = 1
        if not request.POST.get("restaurante") is None:
            encuesta.restaurante = 1
        if not request.POST.get("parque") is None:
            encuesta.parque = 1
        if not request.POST.get("hospital") is None:
            encuesta.hospital = 1
        if not request.POST.get("otro") is None:
            encuesta.otrosLugaresPublicos = 1

        print(request.POST)
        #GUARDAR SIEMPRE Y CUANDO LAS RESPUESTAS NO SEAN NULL
        encuesta.save()
            # Valor Final

        #RECORRER TODAS LAS RESPUESTAS Y SUMARLAS PARA OBTENER UN PUNTUAJE
        puntos = 0
        alumno = User.objects.all().get(matricula=request.user.matricula)
        alumno.puntos = 0

        for k, v in request.POST.items():
            if not k == 'csrfmiddlewaretoken':
                puntos += int(v)
        alumno.puntos += puntos
        alumno.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def Eliminar(request, id):
    obj = Reporte.objects.get(id=id)
    obj.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
 #Reporte.objects.get(id=id).delete()


