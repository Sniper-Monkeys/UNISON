# Generated by Django 3.1.7 on 2021-04-16 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SRRC19', '0025_delete_reporte'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula_reportado', models.CharField(default='xxxxxxxx', max_length=50)),
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
