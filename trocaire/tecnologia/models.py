# -*- coding: utf-8 -*-
from django.db import models
from trocaire.medios.models import CHOICE_SINO, Encuesta 

CHOICE_RIEGO = (
                 (1,'1. No tiene'),
                 (2,'2. Aspersión'),
                 (3,'3. Goteo'),
                 (4,'4. Gravedad'),
                 (5,'5. Otro'),
                 (6, 'Biofiltro')
               )
               
class Riego(models.Model):
    respuesta = models.IntegerField(choices=CHOICE_RIEGO)
    area = models.FloatField('Área regadas en Manzanas', help_text="en manzanas")
    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = "123. Tiene riego (Área regada en metro cuadrado)"
        
CHOICE_CSA = (
                    (1,'1. No tiene'),
                    (2,'2. Granos y hortalizas'),
                    (3,'3. Anuales'),
                    (4,'4. Permanentes'),
                    (5,'5. Pastos'),
                    (6,'6. Área total'),
                    (7, 'Hortalizas')
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
                    (4,'128. Tiene áreas protegidas contra plagas y enfermedades solamente con insecticidas, fungicidas y plaguicidas orgánicos'),
                    (5,'Utiliza preparación de suelo en cama alta'),
                    (6,'Incorpora abonos verdes'),
                    (7,'Utiliza asociación y rotación de cultivos'),
                    (8,'Utiliza cercas vivas'),
                    (9,'Utiliza zanjas de infiltración'),
                    (10,'Utiliza cortinas rompevientos'),
                    (11,'Utiliza labranza cero'),
                    (12,'Utiliza malla antiviral para control de plagas'),
                    (13,'Utiliza variedades resistentes'),
                    (14,'Utiliza lombrihumus'),
                    (15,'Utiliza desinfección de suelo con ceniza y cal'),
                    (16,'Utiliza inoculante'),
                    (17, 'Tiene áreas protegidas contra plagas y enfermedades solamente con insecticidas, fungicidas y plaguicidas biológicas'),
                    (18,'Otros'),
                    )
                    
class UsoTecnologia(models.Model):
    tecnologia = models.IntegerField(choices=CHOICE_TECNOLOGIAS)
    granos = models.IntegerField('Granos y hortalizas', choices=CHOICE_SINO)
    anuales = models.IntegerField('Anuales', choices=CHOICE_SINO)
    permanentes = models.IntegerField('Permanentes', choices=CHOICE_SINO)
    pastos = models.IntegerField('Pastos', choices=CHOICE_SINO)
    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = "Tecnologia utilizada en la producción agropecuaria"
        
CHOICE_MAIZ = (
                    (1,'1. Maíz criollo'),
                    (2,'2. Maíz mejorado'),
                    (3,'3. Otra'),
                    (4,'4. No sembró Maíz'),
                    (5, 'Maiz acriollado'),
                    
               )
CHOICE_FRIJOL = (
                    (1,'1. Frijol criollo'),
                    (2,'2. Frijol mejorado'),
                    (3,'3. Otra'),
                    (4,'4. No sembró Frijol'),
                    (5, 'Frijol acriollado'),
                   
               )
               
class Semilla(models.Model):
    maiz = models.IntegerField('Maíz', choices=CHOICE_MAIZ)
    frijol = models.IntegerField(choices=CHOICE_FRIJOL)
    encuesta = models.ForeignKey(Encuesta)

    class Meta:
        verbose_name_plural = "129. Cuál es el principal tipo de semilla que utilizó para sembrar Maíz y Frijol"       
