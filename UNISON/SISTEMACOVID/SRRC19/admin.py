from django.contrib import admin
from .models import User
from UNISON.SISTEMACOVID.SRRC19.models import *

admin.site.register(User)
admin.site.register(Reporte)
admin.site.register(Encuesta)
admin.site.register(Grupos)
admin.site.register(Profesores)
