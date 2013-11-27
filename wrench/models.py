from django.db import models
import datetime

# Create your models here.

PEOPLE_CHOICES = (
	('BC', 'Brian Connolly'),
	('ID', 'Imran Dossa'),
	('SM', 'Scott Milburn'),
	('SQ', 'Syed Qadri'),
	('RL', 'Rob Lathigee'),	
	('FY', 'Frank Yong'),
)

SEVERITY_CHOICES = (
	('Log', 'Log'),
	('S1', 'Severity 1 - System Down'),
	('S2', 'Severity 2 - Function Inoperable - No Workaround'),
	('S3', 'Severity 3 - Function Inoperable - Workaround Exists'),
	('S4', 'Severity 4 - Nuisance - No Impact to Production'),
	('S5', 'Severity 5 - Enhancement Request'),
	('S6', 'Severity 6 - Information Request'),
)

APPLICATION_AREAS = (
	('PCAD', 'PragmaCAD'),
	('PLINE', 'PragmaLine'),
	('CONNV', 'Connectivity Viewer'),
	('PcAD', 'PragmaCAD'),
)

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
	date_created = models.DateTimeField(datetime.datetime.now())

	def __unicode__(self):
		return self.note

class Incident(models.Model):
	ticket = models.OneToOneField(Ticket)
	assigned_to = models.CharField(max_length=24, choices=PEOPLE_CHOICES)
	date_assigned = models.DateTimeField()
	severity = models.CharField(max_length=100, choices=SEVERITY_CHOICES)

class Change(models.Model):
	incident = models.OneToOneField(Incident)
	start_datetime = models.DateTimeField()
	end_datetime = models.DateTimeField()

