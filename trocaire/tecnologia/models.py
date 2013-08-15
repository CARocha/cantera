# -*- coding: utf-8 -*-
from django.db import models
from trocaire.medios.models import CHOICE_SINO, Encuesta 

CHOICE_RIEGO = (
                 (1,'1. No tiene'),
                 (2,'2. Aspersión'),
                 (3,'3. Goteo'),
                 (4,'4. Biofiltro'),
                 (5,'5. Gravedad'),
                 (6,'6. Otro')
               )
               
class Riego(models.Model):
    respuesta = models.IntegerField(choices=CHOICE_RIEGO)
    area = models.FloatField('Área regadas en m2', help_text="en mtro cuadrado")
    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = "123. Tiene riego (Área regada en metro cuadrado)"
        
CHOICE_CSA = (
                    (1,'1. No tiene'),
                    (2,'2. Granos básicos'),
                    (3,'3. Anuales'),
                    (4,'4. Hortalizas'),
                    (5,'5. Permanentes'),
                    (6,'6. Pastos'),
                    (7,'7. Área total')
               )
               
class AreaProtegida(models.Model):
    respuesta = models.IntegerField(choices=CHOICE_CSA)
    cantidad = models.FloatField('Cantidad protegida en Manzanas', help_text="en manzanas")
    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = "124. Área protegida con obras de CSA (En manzana)"
        
CHOICE_TECNOLOGIAS = (
                    (1,'125. Fertilizo con urea y completo'),
                    (2,'126. Protegió contra plagas, enfermedades con agroquimico. O utilizo de herbicidas'),
                    (3,'127. Tiene áreas fertilizadas solamente con abonos orgánicos'),
                    (4,'128. Tiene áreas protegidas contra plagas y enfermedades solamente con insecticidas, fungicidas y plaguicidas biológicos'),
                    (5,'128. Tiene áreas protegidas contra plagas y enfermedades solamente con insecticidas, fungicidas y plaguicidas'),
                    (6,'Utiliza preparación de suelo en cama alta'),
                    (7,'Incorpora abonos verdes'),
                    (8,'Utiliza asociación y rotación de cultivos'),
                    (9,'Utiliza cercas vivas'),
                    (10,'Utiliza zanjas de infiltración'),
                    (11,'Utiliza cortinas rompevientos'),
                    (12,'Utiliza labranza cero'),
                    (13,'Utiliza malla antiviral para control de plagas'),
                    (14,'Utiliza variedades resistentes'),
                    (15,'Utiliza lombrihumus'),
                    (16,'Utiliza desinfección de suelo con ceniza y cal'),
                    (17,'Utiliza inoculante'),
                    (18,'Otros'),
                    )
                    
class UsoTecnologia(models.Model):
    tecnologia = models.IntegerField(choices=CHOICE_TECNOLOGIAS)
    granos = models.IntegerField('Granos', choices=CHOICE_SINO)
    anuales = models.IntegerField('Anuales', choices=CHOICE_SINO)
    permanentes = models.IntegerField('Permanentes', choices=CHOICE_SINO)
    pastos = models.IntegerField('Pastos', choices=CHOICE_SINO)
    hortaliza = models.IntegerField('Hortalizas', choices=CHOICE_SINO, null=True, blank=True)
    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = "Tecnologia utilizada en la producción agropecuaria"
        
CHOICE_MAIZ = (
                    (1,'1. Maíz criollo'),
                    (2,'2. Maiz acriollado'),
                    (3,'3. Maíz mejorado'),
                    (4,'4. Otra'),
                    (5,'5. No sembró Maíz')     
               )
CHOICE_FRIJOL = (
                    (1,'1. Frijol criollo'),
                    (2, '2. Frijol acriollado'),
                    (3,'3. Frijol mejorado'),
                    (4,'4. Otra'),
                    (5,'5. No sembró Frijol')
               )
               
class Semilla(models.Model):
    maiz = models.IntegerField('Maíz', choices=CHOICE_MAIZ)
    frijol = models.IntegerField(choices=CHOICE_FRIJOL)
    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = "129. Cuál es el principal tipo de semilla que utilizó para sembrar Maíz y Frijol"       
