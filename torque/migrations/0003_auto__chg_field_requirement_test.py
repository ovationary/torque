# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Requirement.test'
        db.alter_column(u'torque_requirement', 'test_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['torque.Test'], null=True))

    def backwards(self, orm):

        # Changing field 'Requirement.test'
        db.alter_column(u'torque_requirement', 'test_id', self.gf('django.db.models.fields.related.ForeignKey')(default='test', to=orm['torque.Test']))

    models = {
        u'torque.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'})
        },
        u'torque.product': {
            'Meta': {'object_name': 'Product'},
            'function': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'torque.productarea': {
            'Meta': {'object_name': 'ProductArea'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['torque.Product']"})
        },
        u'torque.requirement': {
            'Meta': {'object_name': 'Requirement'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'origin': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'product': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['torque.Product']", 'unique': 'True'}),
            'req_type': ('django.db.models.fields.CharField', [], {'default': "'FUNC'", 'max_length': '100'}),
            'sme': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'test': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['torque.Test']", 'null': 'True'})
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