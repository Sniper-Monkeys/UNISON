# Generated by Django 3.1.7 on 2021-04-16 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SRRC19', '0026_reporte'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlumnoBuscado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alumno_buscado', models.CharField(default='xxxxxxxx', max_length=50)),
                ('NoCubrebocas', models.BooleanField(default=False)),
                ('GelSanitizante', models.BooleanField(default=False)),
                ('NoTapeteSanitizante', models.BooleanField(default=False)),
                ('NoRespetarAforo', models.BooleanField(default=False)),
                ('NoRespetarSanaDistancia', models.BooleanField(default=False)),
                ('NoRealizarEncuestaSemanal', models.BooleanField(default=False)),
                ('NoRespetarEstadoDeRiesgo', models.BooleanField(default=False)),
                ('AsistirDiasSeguidos', models.BooleanField(default=False)),
                ('Comentarios', models.CharField(default='...', max_length=255)),
            ],
        ),
    ]
