# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BackgroundImage'
        db.create_table('background_backgroundimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('image_upload', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('background', ['BackgroundImage'])


    def backwards(self, orm):
        # Deleting model 'BackgroundImage'
        db.delete_table('background_backgroundimage')


    models = {
        'background.backgroundimage': {
            'Meta': {'object_name': 'BackgroundImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_upload': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['background']