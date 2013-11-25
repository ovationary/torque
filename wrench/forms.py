# wrench/forms.py
from django import forms
from wrench.models import Ticket

class TicketForm(forms.ModelForm):

	class Meta:
		model=Ticket
		#fields = ('summary', 'description', 'environment', 'urgent', 'date_created')
