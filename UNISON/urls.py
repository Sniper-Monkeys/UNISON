"""UNISON URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from UNISON.SISTEMACOVID.SRRC19.views import inicio, contactar, ingresar, perfil, salida,Mandar_correo, Realizar_Encuesta,Reportar

urlpatterns = [
    path('admin/', admin.site.urls ),
    path('contactar/', contactar, name="contacto"),
    path('', ingresar, name='ingresarpagina'),
    path('inicio/', inicio, name='iniciopagina'),
    path('perfil/', perfil, name="perfilpagina"),
    path('salida', salida, name="salidapagina"),
    path('correo/', Mandar_correo, name="mandarcorreo"),
    path('encuesta/',Realizar_Encuesta, name="encuesta"),
    path('reportar/', Reportar, name="reportar"),
]
