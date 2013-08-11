# -*- coding: utf-8 -*-
from django.db import models
from trocaire.medios.models import CHOICE_SINO, Encuesta 

CHOICE_ALIMENTO = (
                    (1,'Granos'),
                    (2,'Féculas'),
                    (3,'Hortalizas y verduras'),
                    (4,'Frutas'),
                    (5,'Láctios y huevos'),
                    (6,'Carnes'),
                    (7,'Grasas y aceites'),
                    (8,'Otros')
               )
               
class Alimentos(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return self.nombre
               
class Diversidad(models.Model):
    alimento = models.ForeignKey(Alimentos)
    respuesta = models.IntegerField(choices=CHOICE_SINO)
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "Diversidad Alimentaria"

CHOICE_TIEMPO = (
                    (1,'Solo un tiempo(ya sea desayuno, almuerzo o cena)'),
                    (2,'Dos tiempo de comida'),
                    (3,'Los tres tiempo'),
                    (4,'Los tres tiempo y 1 merienda'),
                    (5,'Los tres tiempo y 2 meriendas')
               )

class TiempoComida(models.Model):
    tiempos = models.IntegerField(choices=CHOICE_TIEMPO,null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = "Cuántos tiempos de comida comsumió ayer"