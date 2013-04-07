# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BlogPost.associated_project'
        db.add_column('blog_blogpost', 'associated_project',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['gallery.Gallery']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BlogPost.associated_project'
        db.delete_column('blog_blogpost', 'associated_project_id')


    models = {
        'blog.blogpost': {
            'Meta': {'object_name': 'BlogPost'},
            'associated_project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Gallery']"}),
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
        },
        'gallery.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'description': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'Gallery_description'", 'null': 'True', 'to': "orm['cms.Placeholder']"}),
            'icon': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['blog']