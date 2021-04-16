# Generated by Django 3.1.7 on 2021-04-15 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SRRC19', '0017_auto_20210415_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='CorreoMandado',
            field=models.CharField(choices=[('S', 'SI'), ('N', 'NO')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='riesgo',
            field=models.CharField(choices=[('R', 'Rojo'), ('M', 'Naranja'), ('A', 'Amarillo'), ('V', 'Verde')], default='V', max_length=1),
        ),
    ]