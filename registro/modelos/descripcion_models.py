# -*- coding: utf-8 -*-
from django.db import models

class Descripcion(models.Model):
    """ Descripcion del problema del paciente """
    LIMITACIONES_OPTIONS = ((1, "SI"), (2, "NO"), (3, "DESCONOCE"))
    DESCUBRIO_MOLESTIAS_OPTIONS = [('papa','Papa'),('mama','Mama'),('abuelos','Abuelos'),('otros','Otros')]
    DIFICULTADES_OPTIONS = [('audicion','Audición'),('vision','Visión'),('lenguaje','Lenguaje'),('seguridad_si_mismo','Seguridad en sí mismo'),('comportamiento','Comportamiento'),('alimentacion','Alimentación'),('suenio','Sueño'),('interaccion_social','Interacción social'),('otro','Otro')]
    
    preocupacion = models.CharField(
        "¿Qué le preocupa de su hijo? Algo especial que le llame la atención",
        max_length=500
    )
    disc_molestias = models.CharField(
        "¿Quién descubrió estas molestias?",
        blank=True,
        max_length=256
    )
    edad_disc_molestia = models.PositiveSmallIntegerField(
        "¿A qué edad notaron estas molestias?",
        blank=True
    )
    tratamiento = models.BooleanField("¿Se encuentra en algún tratamiento?")
    lugar_tratamiento = models.CharField("¿Dónde realiza el tratamiento?",
                                         max_length=256, blank=True)
    limitaciones_movimiento = models.IntegerField(
        "¿Existe alguna limitación con sus movimientos?",
        choices=LIMITACIONES_OPTIONS)

    areas_dificultad = models.CharField("¿Ha presentado su hijo(a) algún tipo de dificultad en éstas áreas?",
                                        max_length=256, blank=True)
    had_convulsion = models.SmallIntegerField("¿Ha sentido convulsiones?",
                                              choices=LIMITACIONES_OPTIONS)
    tipo_crisis = models.CharField("¿Qué tipo de crisis tuvo durante la convulsión?",
                                   max_length=256, blank=True)

    edad_crisis = models.PositiveSmallIntegerField("¿A qué edad fue la primera crisis?", blank=True, null=True)

    

class Terapia_Paciente(models.Model):
    """ terapias recibidas por el paciente en kz"""
    TERAPIA_CHOICES = ((1, "REHABILITACIÓN FÍSICA"),
                       (2, "ESTIMULACIÓN TEMPRANA"),
                       (3, "INTEGRACIÓN SENSORIAL"),
                       (4, "HIPOTERAPIA"),
                       (5, "LENGUAJE"),
                       (6, "PSICOPEDAGÓGICA"),
                       (7, "TERAPIA FAMILIAR"),
                       (8, "NINGUNA"))
    tipo = models.SmallIntegerField("Tipo de terapia", choices=TERAPIA_CHOICES)
    costo_sesion = models.PositiveSmallIntegerField(default=1, blank=False, null=False)    
    tiempo_terapia = models.DurationField("¿Cuánto tiempo lleva realizando la terapia")

class Terapia(models.Model):
    """ terapias recibidas por el paciente """
    TERAPIA_CHOICES = ((1, "Rehabilitación Física"),
                       (2, "Estimulación Temprana"),
                       (3, "Ninguna"))
    tipo = models.SmallIntegerField("Tipo de terapia", choices=TERAPIA_CHOICES)   
    tiempo_terapia = models.CharField("¿Cuánto tiempo lleva realizando la terapia", max_length=50)
    descripcion = models.ForeignKey(Descripcion)


class Terapista(models.Model):
    """ Representa el terapista del paciente """
    GRUPO_SANGUINEO_CHOICES = (
        ("A+", "A+"),
        ("A-", "A-"),
        ("O+", "O+"),
        ("O-", "O-"),
        ("B+", "B+"),
        ("B-", "B-"),
        ("AB+", "AB+"), 
        ("AB-", "AB-")        
    )
    cedula = models.CharField(max_length=10)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=256)
    telefonos = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField("fecha de nacimiento")
    grupo_sanguineo = models.CharField("grupo sanguineo",
                                        choices=GRUPO_SANGUINEO_CHOICES,
                                        max_length=4)
    terapia = models.ForeignKey(Terapia_Paciente, null=True, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.apellidos + " " + self.nombres






class Medicamento(models.Model):
    """ Medicamento recetado para convulsiones """
    nombre = models.CharField("nombre del medicamento", max_length=100)
    dosis_diaria = models.IntegerField()
    descripcion = models.ForeignKey(Descripcion)
