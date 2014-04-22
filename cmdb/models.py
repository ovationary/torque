from django.db import models

# Create your models here.
class OperatingSystem(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField(blank=True, null=True)

  def __str__(self):
  	return self.name

class Service(models.Model):
  name = models.CharField(max_length=50)
  description = models.TextField(blank=True, null=True)

  def __str__(self):
  	return self.name


class HardwareComponent(models.Model):
  manufacturer = models.CharField(max_length=50)
  hwtype = models.CharField(max_length=50)
  model = models.CharField(max_length=50, blank=True, null=True)
  vendor_part_number = models.CharField(max_length=50, blank=True, null=True)
  description = models.TextField(blank=True, null=True)

  def __str__(self):
  	return self.manufacturer

  class Server(models.Model):
  	name = models.CharField(max_length=50)
  	description