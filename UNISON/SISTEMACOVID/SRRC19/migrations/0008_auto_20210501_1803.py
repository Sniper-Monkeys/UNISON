# Generated by Django 3.1.7 on 2021-05-02 01:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SRRC19', '0007_auto_20210501_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encuesta',
            name='fecha',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 1, 18, 3, 39, 391271)),
        ),
        migrations.AlterField(
            model_name='reporte',
            name='hora',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 1, 18, 3, 39, 392298)),
        ),
    ]
