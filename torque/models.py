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

class Product(models.Model):
	name = models.CharField(max_length=100)
	function = models.CharField(max_length=100, blank=True)
	version = models.CharField(max_length=25)

	def __unicode__(self):
		return self.name

class ProductArea(models.Model):
	name = models.CharField(max_length=100)
	product = models.ForeignKey(Product)

	def __unicode__(self):
		return self.name

class Requirement(models.Model):
	req_id = models.CharField(max_length=100, unique=True)
	test = models.ForeignKey(Test, null=True)
	REQTYPE_CHOICES = (
		('FUNC', 'Functional'),
		('NONFUNC', 'Non-functional'),
		('NERC','NERC'),
		('FUTURE', 'Future'),
	)
	req_type = models.CharField(max_length=100, choices=REQTYPE_CHOICES, default='FUNC')
	author = models.CharField(max_length=100, blank=True)
	description = models.TextField()
	name = models.CharField(max_length=100)
	sme = models.CharField(max_length=100)
	origin = models.CharField(max_length=100, blank=True)
	productarea = models.OneToOneField(ProductArea)

	def __unicode__(self):
		return self.name




