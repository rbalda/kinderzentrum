# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-21 06:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cita', '0002_auto_20160516_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cita',
            name='fecha_cita',
            field=models.DateField(),
        ),
    ]
