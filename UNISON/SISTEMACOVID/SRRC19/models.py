from django.db import models

#python manage.py createmigrate <- Para almacenar modelo de base de datos
#python manage.py createsuperuser <- Para agregar un super usuario
#python manage.py migrate <- Para actualizar modelo de base de datos
#NO ABRIR UNIVERSIDAD.DB


# Modelos de la base de datos.

class Alumno(models.Model):
    ApellidoPaterno = models.CharField(max_length=35)
    ApellidoMaterno = models.CharField(max_length=35)
    Nombres = models.CharField(max_length=35)
    Matricula = models.CharField(max_length=8)
    SEXO = (('F', 'Femenino'), ('M', 'Masculino'))
    Sexo = models.CharField(max_length=1, choices=SEXO, default='M')

    RIESGO = (('R', 'Rojo'), ('M', 'Naranja'),  ('A', 'Amarillo'), ('V', 'Verde'))
    Riesgo = models.CharField(max_length=1, choices=RIESGO, default='V')

    def NombreCompleto(self):
        cadena = "{0} {1} {2}, {3}"
        return cadena.format(self.ApellidoPaterno, self.ApellidoMaterno, self.Nombres, self.Matricula)

    def Apellidos(self):
        cadena = "{0} {1}"
        return cadena.format((self.ApellidoPaterno, self.ApellidoMaterno))

    def __str__(self):
        return self.NombreCompleto()


class Docente(models.Model):
    ApellidoPaterno = models.CharField(max_length=35)
    ApellidoMaterno = models.CharField(max_length=35)
    Nombres = models.CharField(max_length=35)
    Cedula = models.CharField(max_length=8)
    DiaDeIngreso = models.CharField(max_length=5) #Opcional
    SEXO = (('F', 'Femenino'), ('M', 'Masculino'))
    Sexo = models.CharField(max_length=1, choices=SEXO, default='M')

    def NombreCompleto(self):
        cadena = "{0} {1} {2}, {3}"
        return cadena.format(self.ApellidoPaterno, self.ApellidoMaterno, self.Nombres, self.Cedula)

    def __str__(self):
        return self.NombreCompleto()



class PersonalAdministrativo(models.Model):
    ApellidoPaterno = models.CharField(max_length=35)
    ApellidoMaterno = models.CharField(max_length=35)
    Nombres = models.CharField(max_length=35)
    Cedula = models.CharField(max_length=8)
    DiaDeIngreso = models.CharField(max_length=5) #Opcional
    SEXO = (('F', 'Femenino'), ('M', 'Masculino'))
    Sexo = models.CharField(max_length=1, choices=SEXO, default='M')

    def NombreCompleto(self):
        cadena = "{0} {1} {2}, {3}"
        return cadena.format(self.ApellidoPaterno, self.ApellidoMaterno, self.Nombres, self.Cedula)

    def __str__(self):
        return self.NombreCompleto()