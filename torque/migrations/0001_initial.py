# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Set'
        db.create_table(u'torque_set', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
        ))
        db.send_create_signal(u'torque', ['Set'])

        # Adding model 'Category'
        db.create_table(u'torque_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
        ))
        db.send_create_signal(u'torque', ['Category'])

        # Adding model 'Test'
        db.create_table(u'torque_test', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('testid', self.gf('django.db.models.fields.CharField')(max_length=24)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['torque.Category'])),
            ('testset', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['torque.Set'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('prerequisite', self.gf('django.db.models.fields.TextField')()),
            ('procedure', self.gf('django.db.models.fields.TextField')()),
            ('results', self.gf('django.db.models.fields.TextField')()),
            ('comments', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'torque', ['Test'])

        # Adding model 'Step'
        db.create_table(u'torque_step', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('test', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['torque.Test'])),
            ('stepnum', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('instruction', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'torque', ['Step'])

        # Adding model 'Product'
        db.create_table(u'torque_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=25)),
        ))
        db.send_create_signal(u'torque', ['Product'])

        # Adding model 'Requirement'
        db.create_table(u'torque_requirement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('test', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['torque.Test'])),
            ('req_type', self.gf('django.db.models.fields.CharField')(default='FUNC', max_length=100)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('sme', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('origin', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('product', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['torque.Product'], unique=True)),
        ))
        db.send_create_signal(u'torque', ['Requirement'])


    def backwards(self, orm):
        # Deleting model 'Set'
        db.delete_table(u'torque_set')

        # Deleting model 'Category'
        db.delete_table(u'torque_category')

        # Deleting model 'Test'
        db.delete_table(u'torque_test')

        # Deleting model 'Step'
        db.delete_table(u'torque_step')

        # Deleting model 'Product'
        db.delete_table(u'torque_product')

        # Deleting model 'Requirement'
        db.delete_table(u'torque_requirement')


    models = {
        u'torque.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'torque.product': {
            'Meta': {'object_name': 'Product'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'torque.requirement': {
            'Meta': {'object_name': 'Requirement'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'origin': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'product': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['torque.Product']", 'unique': 'True'}),
            'req_type': ('django.db.models.fields.CharField', [], {'default': "'FUNC'", 'max_length': '100'}),
            'sme': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'test': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['torque.Test']"})
        },
        u'torque.set': {
            'Meta': {'object_name': 'Set'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'torque.step': {
            'Meta': {'object_name': 'Step'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instruction': ('django.db.models.fields.TextField', [], {}),
            'stepnum': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'test': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['torque.Test']"})
        },
        u'torque.test': {
            'Meta': {'object_name': 'Test'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['torque.Category']"}),
            'comments': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prerequisite': ('django.db.models.fields.TextField', [], {}),
            'procedure': ('django.db.models.fields.TextField', [], {}),
            'results': ('django.db.models.fields.TextField', [], {}),
            'testid': ('django.db.models.fields.CharField', [], {'max_length': '24'}),
            'testset': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['torque.Set']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['torque']