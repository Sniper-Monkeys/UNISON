from django.conf import settings
from django.core.mail import send_mail, send_mass_mail
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from datetime import datetime
from django.shortcuts import render, redirect

# python manage.py createmigrate <- Para almacenar modelo de base de datos
# python manage.py createsuperuser <- Para agregar un super usuario
# python manage.py migrate <- Para actualizar modelo de base de datos
# NO ABRIR UNIVERSIDAD.DB

from django.contrib.auth.models import AbstractUser, Group
from django.contrib.auth.models import User
from django.template.loader import render_to_string


class User(AbstractUser):
    matricula = models.CharField(max_length=50, default='xxxxxxxx', verbose_name='Matricula')
    OCUPACION = (('A', 'Alumno'), ('D', 'Docente'), ('P', 'Personal Administrativo'))
    ocupacion = models.CharField(max_length=1, choices=OCUPACION, default='A')
    RIESGO = (('R', 'Rojo'), ('N', 'Naranja'), ('A', 'Amarillo'), ('V', 'Verde'))
    riesgo = models.CharField(max_length=1, choices=RIESGO, default='V', verbose_name='Riesgo')
    CORREOMANDADO = (('S', 'SI'), ('N', 'NO'))
    CorreoMandado = models.CharField(max_length=1, choices=CORREOMANDADO, default='N')
    puntos = models.IntegerField(default=0)

    class Meta:
        ordering = ['ocupacion']

    def CambiarARojo(self):
        self.riesgo = 'R'


@receiver(pre_save, sender=User)
def signal(sender, instance, **kwargs):
    try:
        old_instance = sender.objects.get(pk=instance.pk)
        # SISTEMA PARA MANDAR CORREO CUANDO LOS PUNTOS DEL USUARIO SEAN MAYOR A X PUNTOS
        if old_instance.puntos != instance.puntos:
            if instance.puntos >= 50:
                instance.riesgo = 'R'
            elif 35 <= instance.puntos < 50:
                instance.riesgo = 'N'
            elif 20 <= instance.puntos < 35:
                instance.riesgo = 'A'
            else:
                instance.riesgo = 'V'

        # SISTEMA PARA MANDAR CORREO CUANDO EL USUARIO ESTÉ EN ROJO
        if old_instance.riesgo != instance.riesgo:
            if instance.riesgo == 'R':
                asunto = "¡Persona en Estado de Riesgo Rojo!"
                mensaje = render_to_string('email_template.html',
                                           {'name': instance.get_full_name(),
                                            'expediente': instance.matricula})
                email_desde = settings.EMAIL_HOST_USER
                emails = User.objects.filter(ocupacion="P").exclude(email='').values_list('email')

                emails_para = []
                contador = 0
                for i in emails:
                    emails_para.append(i[contador])
                    contador += 1
                emails_para.append(instance.email)

                grupos = Grupos.objects.all()
                alumnos = []
                for grupo in grupos:
                    alumnos = grupo.users.values()
                    for alumno in alumnos:
                        if alumno['matricula'] == instance.matricula:
                            emails_para.append(grupo.Profesor.Docente.email)
                print(emails_para)
                if len(emails_para) < 4:
                    send_mail(asunto, mensaje, email_desde, emails_para, fail_silently=False)
                elif len(emails_para) > 4:
                    send_mass_mail(asunto, mensaje, email_desde, emails_para)

    except sender.DoesNotExist:
        pass


class Encuesta(models.Model):
    # Información alumno
    matricula_encuestado = models.CharField(max_length=50, default='xxxxxxxx')
    nombre_encuestado = models.CharField(max_length=255, default='xxxxxxxx')
    fecha = models.DateTimeField(default=datetime.now(), blank=True)

    # Problemas de salud

    positivoCovid = models.BooleanField(default=False)
    fiebre = models.IntegerField(default=0)
    gripa = models.IntegerField(default=0)
    tos = models.IntegerField(default=0)
    problemasRespiratorios = models.IntegerField(default=0)
    dolorCabeza = models.IntegerField(default=0)
    dolorMuscular = models.IntegerField(default=0)
    dolorGarganta = models.IntegerField(default=0)
    diarrea = models.IntegerField(default=0)
    perdidaOlfato = models.IntegerField(default=0)
    perdidaGusto = models.IntegerField(default=0)
    cansancio = models.IntegerField(default=0)
    comentariosdificultad = models.CharField(max_length=255, default="...")

    problemaCardiovascular = models.BooleanField(default=False)
    asma = models.BooleanField(default=False)
    cancer = models.BooleanField(default=False)
    diabetes = models.BooleanField(default=False)
    bronquitis = models.BooleanField(default=False)
    otrosProblemas = models.CharField(max_length=255, default="...")

    # Paises
    PersonasContacto = ((1, '1-5'), (2, '5-10'), (3, '10-20'), (4, '20-50'), (5, 'Más de 50'))
    personasContacto = models.IntegerField(choices=PersonasContacto, default=1)

    # LugaresPublicos
    cine = models.BooleanField(default=False)
    centroComercial = models.BooleanField(default=False)
    restaurante = models.BooleanField(default=False)
    parque = models.BooleanField(default=False)
    hospital = models.BooleanField(default=False)
    otrosLugaresPublicos = models.CharField(max_length=255, default="...")

    def __str__(self):
        return self.matricula_encuestado


class Reporte(models.Model):
    matricula_reportado = models.CharField(max_length=50, default='xxxxxxxx')
    NoCubrebocas = models.BooleanField(default=False)
    GelSanitizante = models.BooleanField(default=False)
    NoTapeteSanitizante = models.BooleanField(default=False)
    NoRespetarAforo = models.BooleanField(default=False)
    NoRespetarSanaDistancia = models.BooleanField(default=False)
    NoRealizarEncuestaSemanal = models.BooleanField(default=False)
    NoRespetarEstadoDeRiesgo = models.BooleanField(default=False)
    AsistirDiasSeguidos = models.BooleanField(default=False)
    Comentarios = models.CharField(max_length=255, default="...")
    hora = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.matricula_reportado


class AlumnoBuscado(models.Model):
    alumno_buscado = models.CharField(max_length=50, default='xxxxxxxx')
    NoCubrebocas = models.BooleanField(default=False)
    GelSanitizante = models.BooleanField(default=False)
    NoTapeteSanitizante = models.BooleanField(default=False)
    NoRespetarAforo = models.BooleanField(default=False)
    NoRealizarEncuestaSemanal = models.BooleanField(default=False)
    NoRespetarSanaDistancia = models.BooleanField(default=False)
    NoRespetarEstadoDeRiesgo = models.BooleanField(default=False)
    AsistirDiasSeguidos = models.BooleanField(default=False)
    Comentarios = models.CharField(max_length=255, default="...")

    def __str__(self):
        return self.alumno_buscado

class Profesores(models.Model):
    """Person object"""

    Docente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


    def __str__(self):
        return self.Docente.username

class Grupos(models.Model):
    Materia = models.CharField(max_length=255)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    Profesor = models.ForeignKey(
        Profesores,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.Materia
