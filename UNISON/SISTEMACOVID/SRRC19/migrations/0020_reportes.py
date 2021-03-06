# Generated by Django 3.1.7 on 2021-04-16 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SRRC19', '0019_auto_20210415_1903'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reportes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cubrebocas', models.BooleanField(default=False)),
                ('GelSanitizante', models.BooleanField(default=False)),
                ('TapeteSanitizante', models.BooleanField(default=False)),
                ('NoRespetarAforo', models.BooleanField(default=False)),
                ('NoRespetarSanaDistancia', models.BooleanField(default=False)),
                ('NoRealizarEncuestaSemanal', models.BooleanField(default=False)),
                ('NoRespetarEstadoDeRiesgo', models.BooleanField(default=False)),
                ('AsistirDiasSeguidos', models.BooleanField(default=False)),
                ('Comentarios', models.CharField(default=None, max_length=255)),
            ],
        ),
    ]
