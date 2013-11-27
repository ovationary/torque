# wrench/views.py

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from wrench.forms import TicketForm
from wrench.models import Ticket

def index(request):
	context = RequestContext(request)

	context_dict = {'categories': 'Wrench'}

	return render_to_response('wrench/index.html', context_dict, context)


def add_ticket(request):
	context = RequestContext(request)

	# A HTTP Post?
	if request.method == 'POST':
		form = TicketForm(request.POST)
		# Have we been provided with a valid form?
		if form.is_valid():
			# save the new category to the database
			form.save(commit=True)
			# Now call the index() view
			# The user will be shown the homepage
			return index(request)
		else:
			# The supplied form containted errors - just print them to the terminal
			print form.errors
	else:
		# if the request was not a POST, display the form to enter details
		form = TicketForm()

	# Bad form (or form details), no form supplied
	# Render the form with error messages (if any)
	return render_to_response('wrench/add_ticket.html', {'form':form}, context)

def show_ticket(request):
	#Request our context from the request passed to us
	context = RequestContext(request)
	#Change the underscores in the category name to spaces
	#URLS don't handle spaces well, so we encode them as underscores
	#We can then simply replace the underscores with spaces again to get the name.

	#Create a context dictionary which we can pass to the template rendering engine 
	#We can start by containing the name of thee category passed by the user 
	context_dict = {}
	try:
		#Can we find a category with the given name?
		#If we can't, the .get() method raises a DoesNotExist exception
		#So the .get() method returns one model instance or raises an exception.
		tickets = Ticket.objects.all()

		context_dict['tickets'] = tickets 
		
	except Ticket.DoesNotExist:
	#We get here if we didn't find the specified category
	#Dont' do anything - the template displays the "no category" message for us
		pass

	return render_to_response('wrench/view_tickets.html', context_dict, context)	

def show_single_ticket(request, ticket_id):
	#Request our context from the request passed to us
	context = RequestContext(request)
	#Change the underscores in the category name to spaces
	#URLS don't handle spaces well, so we encode them as underscores
	#We can then simply replace the underscores with spaces again to get the name.

	#Create a context dictionary which we can pass to the template rendering engine 
	#We can start by containing the name of thee category passed by the user 
	context_dict = {}
	try:
		#Can we find a category with the given name?
		#If we can't, the .get() method raises a DoesNotExist exception
		#So the .get() method returns one model instance or raises an exception.
		ticket = Ticket.objects.get(id=ticket_id)

		context_dict['ticket'] = ticket 
		
	except Ticket.DoesNotExist:
	#We get here if we didn't find the specified category
	#Dont' do anything - the template displays the "no category" message for us
		pass

	return render_to_response('wrench/view_single_ticket.html', context_dict, context)