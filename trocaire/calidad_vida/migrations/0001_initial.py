# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Inmigracion'
        db.create_table('calidad_vida_inmigracion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('inmigra', self.gf('django.db.models.fields.IntegerField')()),
            ('mujer', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('hombre', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('calidad_vida', ['Inmigracion'])

        # Adding model 'Codigo'
        db.create_table('calidad_vida_codigo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('calidad_vida', ['Codigo'])

        # Adding model 'AccesoEscuela'
        db.create_table('calidad_vida_accesoescuela', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('acceso', self.gf('django.db.models.fields.IntegerField')()),
            ('fem_estudia', self.gf('django.db.models.fields.IntegerField')()),
            ('fem_no_estudia', self.gf('django.db.models.fields.IntegerField')()),
            ('mas_estudia', self.gf('django.db.models.fields.IntegerField')()),
            ('mas_no_estudia', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('calidad_vida', ['AccesoEscuela'])

        # Adding model 'RazonesNoEstudia'
        db.create_table('calidad_vida_razonesnoestudia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('acceso', self.gf('django.db.models.fields.IntegerField')()),
            ('fem_no_estudia', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Ni\xc3\xb1as No estudian', to=orm['calidad_vida.Codigo'])),
            ('mas_no_estudia', self.gf('django.db.models.fields.related.ForeignKey')(related_name='Ni\xc3\xb1os No estudian', to=orm['calidad_vida.Codigo'])),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('calidad_vida', ['RazonesNoEstudia'])

        # Adding model 'Abastece'
        db.create_table('calidad_vida_abastece', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('calidad_vida', ['Abastece'])

        # Adding model 'Agua'
        db.create_table('calidad_vida_agua', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sistema', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['calidad_vida.Abastece'])),
            ('calidad', self.gf('django.db.models.fields.IntegerField')()),
            ('clorada', self.gf('django.db.models.fields.IntegerField')()),
            ('tiene', self.gf('django.db.models.fields.IntegerField')()),
            ('tiempo', self.gf('django.db.models.fields.IntegerField')()),
            ('techo', self.gf('django.db.models.fields.IntegerField')()),
            ('piso', self.gf('django.db.models.fields.IntegerField')()),
            ('paredes', self.gf('django.db.models.fields.IntegerField')()),
            ('servicio', self.gf('django.db.models.fields.IntegerField')()),
            ('cuartos', self.gf('django.db.models.fields.IntegerField')()),
            ('estado', self.gf('django.db.models.fields.IntegerField')()),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('calidad_vida', ['Agua'])


    def backwards(self, orm):
        # Deleting model 'Inmigracion'
        db.delete_table('calidad_vida_inmigracion')

        # Deleting model 'Codigo'
        db.delete_table('calidad_vida_codigo')

        # Deleting model 'AccesoEscuela'
        db.delete_table('calidad_vida_accesoescuela')

        # Deleting model 'RazonesNoEstudia'
        db.delete_table('calidad_vida_razonesnoestudia')

        # Deleting model 'Abastece'
        db.delete_table('calidad_vida_abastece')

        # Deleting model 'Agua'
        db.delete_table('calidad_vida_agua')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'calidad_vida.abastece': {
            'Meta': {'object_name': 'Abastece'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'calidad_vida.accesoescuela': {
            'Meta': {'object_name': 'AccesoEscuela'},
            'acceso': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'fem_estudia': ('django.db.models.fields.IntegerField', [], {}),
            'fem_no_estudia': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mas_estudia': ('django.db.models.fields.IntegerField', [], {}),
            'mas_no_estudia': ('django.db.models.fields.IntegerField', [], {})
        },
        'calidad_vida.agua': {
            'Meta': {'object_name': 'Agua'},
            'calidad': ('django.db.models.fields.IntegerField', [], {}),
            'clorada': ('django.db.models.fields.IntegerField', [], {}),
            'cuartos': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'estado': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'paredes': ('django.db.models.fields.IntegerField', [], {}),
            'piso': ('django.db.models.fields.IntegerField', [], {}),
            'servicio': ('django.db.models.fields.IntegerField', [], {}),
            'sistema': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['calidad_vida.Abastece']"}),
            'techo': ('django.db.models.fields.IntegerField', [], {}),
            'tiempo': ('django.db.models.fields.IntegerField', [], {}),
            'tiene': ('django.db.models.fields.IntegerField', [], {})
        },
        'calidad_vida.codigo': {
            'Meta': {'object_name': 'Codigo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'calidad_vida.inmigracion': {
            'Meta': {'object_name': 'Inmigracion'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'hombre': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inmigra': ('django.db.models.fields.IntegerField', [], {}),
            'mujer': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'calidad_vida.razonesnoestudia': {
            'Meta': {'object_name': 'RazonesNoEstudia'},
            'acceso': ('django.db.models.fields.IntegerField', [], {}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'fem_no_estudia': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Ni\\xc3\\xb1as No estudian'", 'to': "orm['calidad_vida.Codigo']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mas_no_estudia': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Ni\\xc3\\xb1os No estudian'", 'to': "orm['calidad_vida.Codigo']"})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'lugar.comarca': {
            'Meta': {'object_name': 'Comarca'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'lugar.departamento': {
            'Meta': {'object_name': 'Departamento'},
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True'})
        },
        'lugar.municipio': {
            'Meta': {'ordering': "['departamento__nombre']", 'object_name': 'Municipio'},
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Departamento']"}),
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True'})
        },
        'medios.contraparte': {
            'Meta': {'object_name': 'Contraparte'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'medios.encuesta': {
            'Meta': {'object_name': 'Encuesta'},
            'beneficiario': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'comarca': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['lugar.Comarca']"}),
            'contraparte': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Contraparte']", 'null': 'True', 'blank': 'True'}),
            'credito': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'encuestador': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Recolector']"}),
            'fecha': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'sexo_jefe': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'medios.recolector': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Recolector'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['calidad_vida']