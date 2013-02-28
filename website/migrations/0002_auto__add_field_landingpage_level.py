# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'LandingPage.level'
        db.add_column(u'website_landingpage', 'level',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'LandingPage.level'
        db.delete_column(u'website_landingpage', 'level')


    models = {
        u'website.landingpage': {
            'Meta': {'object_name': 'LandingPage'},
            'comment': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'variation': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'})
        }
    }

    complete_apps = ['website']