# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Calendar'
        db.create_table(u'iw_calendar', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
        ))
        db.send_create_signal(u'iw', ['Calendar'])

        # Adding model 'Event'
        db.create_table(u'iw_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('start', self.gf('django.db.models.fields.DateTimeField')()),
            ('end', self.gf('django.db.models.fields.DateTimeField')()),
            ('calendar', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['iw.Calendar'])),
        ))
        db.send_create_signal(u'iw', ['Event'])

        # Adding model 'msg'
        db.create_table(u'iw_msg', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('msg', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'iw', ['msg'])


    def backwards(self, orm):
        # Deleting model 'Calendar'
        db.delete_table(u'iw_calendar')

        # Deleting model 'Event'
        db.delete_table(u'iw_event')

        # Deleting model 'msg'
        db.delete_table(u'iw_msg')


    models = {
        u'iw.calendar': {
            'Meta': {'ordering': "['name']", 'object_name': 'Calendar'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'iw.event': {
            'Meta': {'ordering': "['start', 'end']", 'object_name': 'Event'},
            'calendar': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['iw.Calendar']"}),
            'end': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'iw.msg': {
            'Meta': {'object_name': 'msg'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'msg': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['iw']