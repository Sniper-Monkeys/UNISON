# Generated by Django 3.1.7 on 2021-04-15 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SRRC19', '0012_auto_20210414_2052'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='riesgo',
            field=models.CharField(choices=[('R', 'Rojo'), ('M', 'Naranja'), ('A', 'Amarillo'), ('V', 'Verde')], default='V', max_length=1),
        ),
    ]