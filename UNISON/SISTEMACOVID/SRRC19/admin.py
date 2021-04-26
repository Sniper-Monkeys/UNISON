from django.contrib import admin
from .models import User
from UNISON.SISTEMACOVID.SRRC19.models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('matricula','ocupacion','first_name', 'last_name',  'riesgo', 'email')


class survey(admin.ModelAdmin):
    list_display = ('matricula_encuestado', 'nombre_encuestado', 'fecha')


class report(admin.ModelAdmin):
    list_display = ('matricula_reportado', 'hora')

class docentes(admin.ModelAdmin):
    list_display = ('Materia', 'Profesor')
admin.site.register(User,UserAdmin)
admin.site.register(Reporte,report)
admin.site.register(Encuesta,survey)
admin.site.register(Grupos,docentes)
admin.site.register(Profesores)

