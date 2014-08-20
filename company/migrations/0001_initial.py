# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Profile'
        db.create_table(u'company_profile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('about', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('terms', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('location', self.gf('geoposition.fields.GeopositionField')(max_length=42, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('facebook', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('phone_no1', self.gf('django.db.models.fields.CharField')(max_length=12, blank=True)),
            ('phone_no2', self.gf('django.db.models.fields.CharField')(max_length=12, blank=True)),
            ('phone_no3', self.gf('django.db.models.fields.CharField')(max_length=12, blank=True)),
            ('phone_no4', self.gf('django.db.models.fields.CharField')(max_length=12, blank=True)),
            ('phone_no5', self.gf('django.db.models.fields.CharField')(max_length=12, blank=True)),
            ('phone_no6', self.gf('django.db.models.fields.CharField')(max_length=12, blank=True)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(default='banner-default.jpg', max_length=100)),
            ('banner', self.gf('django.db.models.fields.files.ImageField')(default='banner-default.jpg', max_length=100)),
        ))
        db.send_create_signal(u'company', ['Profile'])


    def backwards(self, orm):
        # Deleting model 'Profile'
        db.delete_table(u'company_profile')


    models = {
        u'company.profile': {
            'Meta': {'object_name': 'Profile'},
            'about': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'banner': ('django.db.models.fields.files.ImageField', [], {'default': "'banner-default.jpg'", 'max_length': '100'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'facebook': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('geoposition.fields.GeopositionField', [], {'max_length': '42', 'blank': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'default': "'banner-default.jpg'", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone_no1': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'phone_no2': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'phone_no3': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'phone_no4': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'phone_no5': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'phone_no6': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'terms': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['company']