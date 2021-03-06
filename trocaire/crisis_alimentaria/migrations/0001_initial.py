# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'EstrategiaCrisis'
        db.create_table('crisis_alimentaria_estrategiacrisis', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('crisis_alimentaria', ['EstrategiaCrisis'])

        # Adding model 'Crisis'
        db.create_table('crisis_alimentaria_crisis', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('escases', self.gf('django.db.models.fields.IntegerField')()),
            ('causa', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('crisis_alimentaria', ['Crisis'])

        # Adding M2M table for field enfrentar on 'Crisis'
        db.create_table('crisis_alimentaria_crisis_enfrentar', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('crisis', models.ForeignKey(orm['crisis_alimentaria.crisis'], null=False)),
            ('estrategiacrisis', models.ForeignKey(orm['crisis_alimentaria.estrategiacrisis'], null=False))
        ))
        db.create_unique('crisis_alimentaria_crisis_enfrentar', ['crisis_id', 'estrategiacrisis_id'])

        # Adding model 'Credito'
        db.create_table('crisis_alimentaria_credito', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('crisis_alimentaria', ['Credito'])

        # Adding model 'AccesoCredito'
        db.create_table('crisis_alimentaria_accesocredito', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('encuesta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['medios.Encuesta'])),
        ))
        db.send_create_signal('crisis_alimentaria', ['AccesoCredito'])

        # Adding M2M table for field hombre on 'AccesoCredito'
        db.create_table('crisis_alimentaria_accesocredito_hombre', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('accesocredito', models.ForeignKey(orm['crisis_alimentaria.accesocredito'], null=False)),
            ('credito', models.ForeignKey(orm['crisis_alimentaria.credito'], null=False))
        ))
        db.create_unique('crisis_alimentaria_accesocredito_hombre', ['accesocredito_id', 'credito_id'])

        # Adding M2M table for field mujer on 'AccesoCredito'
        db.create_table('crisis_alimentaria_accesocredito_mujer', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('accesocredito', models.ForeignKey(orm['crisis_alimentaria.accesocredito'], null=False)),
            ('credito', models.ForeignKey(orm['crisis_alimentaria.credito'], null=False))
        ))
        db.create_unique('crisis_alimentaria_accesocredito_mujer', ['accesocredito_id', 'credito_id'])

        # Adding M2M table for field otro_hombre on 'AccesoCredito'
        db.create_table('crisis_alimentaria_accesocredito_otro_hombre', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('accesocredito', models.ForeignKey(orm['crisis_alimentaria.accesocredito'], null=False)),
            ('credito', models.ForeignKey(orm['crisis_alimentaria.credito'], null=False))
        ))
        db.create_unique('crisis_alimentaria_accesocredito_otro_hombre', ['accesocredito_id', 'credito_id'])

        # Adding M2M table for field otra_mujer on 'AccesoCredito'
        db.create_table('crisis_alimentaria_accesocredito_otra_mujer', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('accesocredito', models.ForeignKey(orm['crisis_alimentaria.accesocredito'], null=False)),
            ('credito', models.ForeignKey(orm['crisis_alimentaria.credito'], null=False))
        ))
        db.create_unique('crisis_alimentaria_accesocredito_otra_mujer', ['accesocredito_id', 'credito_id'])


    def backwards(self, orm):
        # Deleting model 'EstrategiaCrisis'
        db.delete_table('crisis_alimentaria_estrategiacrisis')

        # Deleting model 'Crisis'
        db.delete_table('crisis_alimentaria_crisis')

        # Removing M2M table for field enfrentar on 'Crisis'
        db.delete_table('crisis_alimentaria_crisis_enfrentar')

        # Deleting model 'Credito'
        db.delete_table('crisis_alimentaria_credito')

        # Deleting model 'AccesoCredito'
        db.delete_table('crisis_alimentaria_accesocredito')

        # Removing M2M table for field hombre on 'AccesoCredito'
        db.delete_table('crisis_alimentaria_accesocredito_hombre')

        # Removing M2M table for field mujer on 'AccesoCredito'
        db.delete_table('crisis_alimentaria_accesocredito_mujer')

        # Removing M2M table for field otro_hombre on 'AccesoCredito'
        db.delete_table('crisis_alimentaria_accesocredito_otro_hombre')

        # Removing M2M table for field otra_mujer on 'AccesoCredito'
        db.delete_table('crisis_alimentaria_accesocredito_otra_mujer')


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
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'crisis_alimentaria.accesocredito': {
            'Meta': {'object_name': 'AccesoCredito'},
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'hombre': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'Hombre'", 'symmetrical': 'False', 'to': "orm['crisis_alimentaria.Credito']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mujer': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'Mujer'", 'symmetrical': 'False', 'to': "orm['crisis_alimentaria.Credito']"}),
            'otra_mujer': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'Mujer vive'", 'symmetrical': 'False', 'to': "orm['crisis_alimentaria.Credito']"}),
            'otro_hombre': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'Hombre vive'", 'symmetrical': 'False', 'to': "orm['crisis_alimentaria.Credito']"})
        },
        'crisis_alimentaria.credito': {
            'Meta': {'object_name': 'Credito'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'crisis_alimentaria.crisis': {
            'Meta': {'object_name': 'Crisis'},
            'causa': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'encuesta': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['medios.Encuesta']"}),
            'enfrentar': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['crisis_alimentaria.EstrategiaCrisis']", 'null': 'True', 'blank': 'True'}),
            'escases': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'crisis_alimentaria.estrategiacrisis': {
            'Meta': {'object_name': 'EstrategiaCrisis'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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

    complete_apps = ['crisis_alimentaria']