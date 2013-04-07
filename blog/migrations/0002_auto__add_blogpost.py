# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BlogPost'
        db.create_table('blog_blogpost', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('post_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('featured_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('content_area', self.gf('django.db.models.fields.related.ForeignKey')(related_name='content_area', null=True, to=orm['cms.Placeholder'])),
        ))
        db.send_create_signal('blog', ['BlogPost'])


    def backwards(self, orm):
        # Deleting model 'BlogPost'
        db.delete_table('blog_blogpost')


    models = {
        'blog.blogpost': {
            'Meta': {'object_name': 'BlogPost'},
            'content_area': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'content_area'", 'null': 'True', 'to': "orm['cms.Placeholder']"}),
            'featured_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['blog']