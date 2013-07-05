# -*- coding: utf-8 -*-
from django.db import models
from trocaire.medios.models import Encuesta 

CHOICE_CIUDADANA = (
                    (1,'143. CPC'),
                    (2,'144. Asamblea comunitaria'),
                    (3,'-. Comité comarca'),
                    (4,'-. CAPS'),
                    (5,'-. Cooperativa'),
                    (6,'-. Gabinete familiar'),
                    (7,'-. Asamblea Comunitaria'),
                    (8,'-. Iglesia'),

                    )
CHOICE_CIUDADANA_RESPUESTA = (
                                (1,'Son muy beneficioso'),
                                (2,'Hacen algunas cosas'),
                                (3,'No hacen nada'),
                                (4,'NS NR'),
                                (5,'Producción Agroecológica'),
                                (6,'Conservación de recursos agua'),
                                (7,'Medidas de adaptación al cambio climático'),
                                (8,'Jornadas de limpieza y salud'),
                                (9,'Reforestación'),
                              ) 
               
CHOICE_CIUDADANA_DOS = (
                    (1,'145. CPC'),
                    (2,'146. Asamblea comunitaria'),
                    (3,'Iglesia'),
                    (4,'Cantera'),
                    (5,'Comité comarcal'),
                    (6,'Cooperativa'),
                    (7,'Gabinete familiar'),
                    (8,'CAPS'),
                    (9,'CLS'),
                    (10, 'Otros'),
                   
                       )
               
CHOICE_CIUDADANA_TRES = (
                    (1,'147. CPC'),
                    (2,'148. Asamblea comunitaria')
                    
               )

CHOICE_CIUDADANA_TRES_RESPUESTA = (
                    (1,'Lo hacen con frecuencia'),
                    (2,'Algunas veces'),
                    (3,'Muy poco o nunca lo hacen'),
                    (4,'No aplica. No participan')
                    
               )    

class Participacion(models.Model):
    organismo = models.IntegerField(choices=CHOICE_CIUDADANA)
    respuesta = models.IntegerField(choices=CHOICE_CIUDADANA_RESPUESTA)
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "Podria decirnos si esto organismo que le vamos a mencionar promueven la protección al medio ambiente y adaptación al cambio climático y de qué manera"

class ParticipacionCPC(models.Model):
    organismo = models.IntegerField(choices=CHOICE_CIUDADANA_DOS)
    hombre = models.IntegerField()
    mujer = models.IntegerField()
    ambos = models.IntegerField()
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "Quien de la familia participa en los CPC y AC"
        
class Frecuencia(models.Model):
    organismo = models.IntegerField(choices=CHOICE_CIUDADANA_TRES)
    respuesta = models.IntegerField(choices=CHOICE_CIUDADANA_TRES_RESPUESTA)
    encuesta = models.ForeignKey(Encuesta)
    class Meta:
        verbose_name_plural = "Podria decirnos con que frecuencia participan en estas estructuras"       
