# wrench/forms.py
from django import forms
from wrench.models import Ticket, ENVIRONMENT_CHOICES
from django.forms.extras.widgets import SelectDateWidget

class TicketForm(forms.ModelForm):
	summary = forms.CharField(max_length=255, help_text="Please enter a summary of the request: ")
	description = forms.CharField(max_length=255, help_text="Enter a description of the problem: ")
	environment = forms.CharField(max_length=10, widget=forms.Select(choices=ENVIRONMENT_CHOICES), help_text="Which environment were you using? ")
	urgent = forms.BooleanField(help_text="Is this an urgent request? ")
	date_created = forms.DateField(widget=SelectDateWidget(), help_text="Date created: ")

	class Meta:

		model=Ticket
		#fields = ('summary', 'description', 'environment', 'urgent', 'date_created')
