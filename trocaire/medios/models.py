# -*- coding: utf-8 -*-
from django.db import models
from trocaire.lugar.models import *
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey

class Recolector(models.Model):
    nombre = models.CharField(max_length=200)
    def __unicode__(self):
        return u'%s' % self.nombre
    class Meta:
        ordering = ['nombre']
        
class Contraparte(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "Contrapartes Trocaire"

class Encuesta(models.Model):
    ''' Modelo de encuesta principal
    '''
    fecha = models.IntegerField("año de encuesta")
    municipio = models.ForeignKey(Municipio, verbose_name="Nombre del Municipio")
    #comarca = models.ForeignKey(Comarca, verbose_name="Nombre de la comarca/barrio")
    comarca = ChainedForeignKey(
        Comarca, 
        chained_field="municipio",
        chained_model_field="municipio", 
        show_all=False, 
        auto_choose=True
    )
    beneficiario = models.CharField('Nombre del Beneficiario/a', max_length=200)
    encuestador = models.ForeignKey(Recolector, verbose_name="Nombre del encuestador")
    contraparte = models.ForeignKey(Contraparte, null=True, blank=True)
    usuario = models.ForeignKey(User)
    
    #campos ocultos para efectos de querys
    sexo_jefe = models.IntegerField(default=0, editable=False)
    #credito si: 1, credito no: 2
    credito = models.IntegerField(default=2, editable=False)

    def __unicode__(self):
        return self.beneficiario

    class Meta:
        verbose_name_plural = "Encuesta Linea base"

#Utilitarios para toda la encuesta
CHOICE_SEXO = (
                    (1, '1) Masculino'),
                    (2, '2) Femenino')
              )
              
CHOICE_CIVIL = (
                    (1, '1) Casado/a'),
                    (2, '2) Soltero/a'),
                    (3, '3) Viudo/a'),
                    (4, '4) Unión libre')
                )
              
CHOICE_JEFE = (
                    (1, '1) Si'),
                    (2, '2) No'),
                    (3, '3) Compartida')
              )
CHOICE_RELACION = (
                    (1, '1) Conyugue'),
                    (2, '2) Madre/Padre'),
                    (3, '3) Hijo/Hija'),
                    (4, '4) Otro/a'),
                    (5, '5) No aplica')
                  )
                  
CHOICE_SEXO_JEFE = (
                    (1, '1) Masculino'),
                    (2, '2) Femenino'),
                    (3, '3) Compartido'),
                    (4, '4) No aplica')
                   )
                   
CHOICE_DESCRIPCION = (
    (1, '8. Número de personas que viven en el hogar'),
    (2, '9. Número de niñas y niños entre 0 y 10 que viven en el hogar...'),
    (3, '10. Número personas entre 18 y 60 años en el hogar...'),
    (4, '11. Número personas 61 años y más en el hogar familiar...'),
    (5, '12. Número de personas entre 18 y 60 años en el hogar familiar con discapacidad o deficiencia imposibilitados de trabajar...'),
    (6, 'Número de niñas y niños entre 11 y 17 que viven en el hogar...'),
)

# II calidad de vida apps calidad_vida

CHOICE_INMIGRACION = (
    (1, '-. En el último año alguien de la familia salió a trabajar al exterior y regresó'),
    (2, '-. En el último año alguien de la familia salió a trabajar al exterior y no ha regresado, pero mantiene contacto'),
    (3, '-. En el último año alguien de la familia salió a trabajar en otrolugar de Nicaragua y regresa'),
    (4, '-. Su conjugue... tiene más de un año de haber salido a trabajar y no regresado'),
    (5, '-. no aplica')
)

CHOICE_ACCESO = (
    (1, '20. Número de niñas/os entre 6 y 17 años con discapacidad o deficiencia imposibilitados de ir a la escuela'),
    (2, '21. Número de niñas/os entre 6 y 14 años No incluye con discapacidad o deficiencia. Cuántos estudian o no estudian.'),
    (3, '23. Número de niñas/os entre 15 y 17 años. No incluye con discapacidad o deficiencia. ')
    
)

CHOICE_CALIDAD = (
                    (1, '1) Si'),
                    (2, '2) No'),
                    (3, '3) No sabe')
                 )
                 
CHOICE_CLORADA = (
                    (1, '1) Le da tratamiento'),
                    (2, '2) No le da tratamiento'),
                    (3, '3) No aplica. Viene clorada')
                 )
                 
CHOICE_TIEMPO = (
                    (1, '1) Menos de 30 minutos'),
                    (2, '2) 30 minutos a 1 hora'),
                    (3, '3) Más de 1 hora'),
                    (4, '4) Tiene agua en casa')
                  )                 
CHOICE_SINO = (
                    (1, '1) Si'),
                    (2, '2) No'),
                    (3, '3) No aplica')
                 )                                  

CHOICE_TECHO = (
                    (1, '1) Zinc o NIcalit'),
                    (2, '2) Tejas y otros'),
                    (3, '3) Paja o ripios'),
                    (4, '4) Plástico')
                 )
                 
CHOICE_PISO = (
                    (1, '1) Ladrillo, Cemento'),
                    (2, '2) Tierra y encalichado'),
                    (3, '3) Tierra')
                 )
                 
CHOICE_PAREDES = (
                    (1, '1) Ladrillo, bloque, adobe, talquezal mejorado'),
                    (2, '2) Talquezal'),
                    (3, '3) Minifalda'),
                    (4, '4) Ripio')
                 )         
             
CHOICE_SERVICIO = (
                    (1, '1) Inodoro'),
                    (2, '2) Letrina'),
                    (3, '3) No tiene')
                 )   
                 
CHOICE_ESTADO = (
                    (1, '1) Buen estado'),
                    (2, '2) Regular'),
                    (3, '3) En muy mal estado')
                 )
                 
# III FORMAS DE PROPIEDAD

CHOICE_AREA = (
    (1, '36. Área total en manzanas de la propiedad agropecuaria familiar'),
    (2, '37. De esta propiedad... Posee titulo real inscrito en el registro de la propiedad'),
    (3, '38. Posee un titulo entregado por el gobierno... y no lo ha inscrito.'),
    (4, '39. Posee un documento no inscrito(compra venta, herencia,otro)'),
    (5, '40. No posee ningún titulo de respaldo'),
    (6, '41. Si no vive en la propiedad agropecuaria donde trabaja. cuanto es el area del lote donde vive.'),
    (7, '42. Posee titulo real inscrito en el registro de este lote. Poner el area que tiene con titulo real...')
)

# IV PRODUCCION                    

CHOICE_CALIDAD_PATIO = (
                    (1, '1. Diversificado: se usa bien:produce hortaliza, verduras y frutas y genera excendentes'),
                    (2, '2. Capacidad media. Hay sub-utilización del patio. produce solo para auto-consumo'),
                    (3, '3. Sin capacidad. No lo aprovecha')
                 )

