from django.db import models

# Create your models here.

class Set(models.Model):
	name = models.CharField(max_length=128, unique=True)

	def __unicode__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)

	def __unicode__(self):
		return self.name

class Test(models.Model):
	testid = models.CharField(max_length=24)
	category = models.ForeignKey(Category)
	testset = models.ForeignKey(Set)
	title = models.CharField(max_length=128)
	description = models.TextField()
	prerequisite = models.TextField()
	procedure = models.TextField()
	results = models.TextField()
	comments = models.TextField()

	def __unicode__(self):
		return self.title

class Step(models.Model):
	test = models.ForeignKey(Test)
	stepnum = models.IntegerField(blank=True)
	instruction = models.TextField()

	def __unicode__(self):
		return self.instruction


