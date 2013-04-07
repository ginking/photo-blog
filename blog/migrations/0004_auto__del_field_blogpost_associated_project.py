# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'BlogPost.associated_project'
        db.delete_column('blog_blogpost', 'associated_project_id')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'BlogPost.associated_project'
        raise RuntimeError("Cannot reverse this migration. 'BlogPost.associated_project' and its values cannot be restored.")

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