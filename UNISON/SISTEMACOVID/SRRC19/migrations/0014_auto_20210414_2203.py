# Generated by Django 3.1.7 on 2021-04-15 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SRRC19', '0013_user_riesgo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='matricula',
            field=models.CharField(default='xxxxxxxx', max_length=50),
        ),
    ]