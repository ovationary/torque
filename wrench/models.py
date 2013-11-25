from django.db import models
import datetime

# Create your models here.
ENVIRONMENT_CHOICES = (
	('PROD','Production'),
	('QA','Quality Assurance'),
	('MAIN','Maintenance'),
	('TRAIN','Training'),
	('DEV','ASM Development'),
	('INERGI-DEV','Inergi Test Bed'),
)

STATUS_CHOICES = (
	('NEW', 'NEW'),
	('REVIEW', 'UNDER REVIEW'),
	('VENDOR', 'UNDER VENDOR REVIEW'),
	('FIXED', 'FIXED'),
	('HOLD', 'ON HOLD'),
	('CLOSED', 'CLOSED'),		
	)

class Ticket(models.Model):
	summary = models.CharField(max_length=255, unique=True)
	description = models.TextField()
	environment = models.CharField(max_length=10, choices=ENVIRONMENT_CHOICES)
	urgent = models.BooleanField(default=False)
	date_created = models.DateTimeField()

	def __unicode__(self):
		return self.summary

class TicketStatus(models.Model):
	ticket = models.ForeignKey(Ticket)
	status = models.CharField(max_length=24, choices=STATUS_CHOICES)

	def __unicode__(self):
		return self.summary

class TicketAction(models.Model):
	ticket = models.ForeignKey(Ticket)
	note = models.TextField()
	date_created = models.DateTimeField()

	def __unicode__(self):
		return self.note




