# Generated by Django 3.1.7 on 2021-04-16 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SRRC19', '0022_auto_20210416_1204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reporte',
            old_name='Cubrebocas',
            new_name='NoCubrebocas',
        ),
        migrations.RenameField(
            model_name='reporte',
            old_name='TapeteSanitizante',
            new_name='NoTapeteSanitizante',
        ),
        migrations.AlterField(
            model_name='reporte',
            name='Comentarios',
            field=models.CharField(default='...', max_length=255),
        ),
    ]
