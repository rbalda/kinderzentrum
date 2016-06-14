# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 07:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asistencia', '__first__'),
        ('registro', '0002_auto_20160411_2057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_registro', models.DateField(auto_now_add=True)),
                ('fecha_cita', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('estado', models.CharField(choices=[(b'A', b'Agendada'), (b'S', b'Asistio'), (b'N', b'No asistio'), (b'C', b'Cancelada')], default=b'A', max_length=2)),
                ('indicaciones', models.CharField(max_length=256)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.Paciente')),
                ('terapista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asistencia.Terapista')),
                ('tipo_terapia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asistencia.Tipo_terapia')),
            ],
        ),
    ]
