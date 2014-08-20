# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Series'
        db.create_table(u'series_series', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('make', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['make.Make'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default='banner-default.jpg', max_length=100)),
            ('hover_image', self.gf('django.db.models.fields.files.ImageField')(default='banner-default.jpg', max_length=100)),
            ('banner', self.gf('django.db.models.fields.files.ImageField')(default='banner-default.jpg', max_length=100)),
        ))
        db.send_create_signal(u'series', ['Series'])


    def backwards(self, orm):
        # Deleting model 'Series'
        db.delete_table(u'series_series')


    models = {
        u'make.make': {
            'Meta': {'object_name': 'Make'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'banner-default.jpg'", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'series.series': {
            'Meta': {'object_name': 'Series'},
            'banner': ('django.db.models.fields.files.ImageField', [], {'default': "'banner-default.jpg'", 'max_length': '100'}),
            'hover_image': ('django.db.models.fields.files.ImageField', [], {'default': "'banner-default.jpg'", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'banner-default.jpg'", 'max_length': '100'}),
            'make': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['make.Make']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['series']