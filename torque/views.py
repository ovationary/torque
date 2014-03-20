# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from torque.models import Category, Test, Set, Step, Requirement
from torque.forms import CategoryForm, TestForm, UserForm, RequirementForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect 
from django.contrib.auth.decorators import login_required 
from datetime import datetime
from django.views.generic import ListView, CreateView, UpdateView
from django.core.urlresolvers import reverse



class CreateRequirementView(CreateView):
	model = Requirement
	template_name="edit_requirement.html"

	def get_success_url(self):
		return reverse('requirement-list')

	def get_context_data(self, **kwargs):
		context = super(CreateRequirementView, self).get_context_data(**kwargs)
		context['action'] = reverse('requirement-new')
		return context

class ListRequirementsView(ListView):
	model = Requirement
	template_name="requirement_list.html"

class UpdateRequirementView(UpdateView):

	model = Requirement
	template_name = "edit_requirement.html"

	def get_success_url(self):
		return reverse("requirement-list")

	def get_context_data(self, **kwargs):
		context = super(UpdateRequirementView, self).get_context_data(**kwargs)
		context['action'] = reverse('requirement-edit', kwargs={'pk': self.get_object().id})

		return context
		


def index(request):
	context = RequestContext(request)

	category_list = Category.objects.all()
	context_dict = {'categories': category_list}

	for category in category_list:
		category.url = category.name.replace(' ','_')

	req_list = Requirement.objects.order_by('name')
	test_list = Test.objects.order_by('title')

	context_dict['requirements']=req_list
	context_dict['tests'] = test_list

	return render_to_response('torque/index.html', context_dict, context)

def category(request, category_name_url):
	#Request our context from the request passed to us
	context = RequestContext(request)
	#Change the underscores in the category name to spaces
	#URLS don't handle spaces well, so we encode them as underscores
	#We can then simply replace the underscores with spaces again to get the name.

	category_name = category_name_url.replace('_','')

	#Create a context dictionary which we can pass to the template rendering engine 
	#We can start by containing the name of thee category passed by the user 
	context_dict = {'category_name': category_name}

	try:
		#Can we find a category with the given name?
		#If we can't, the .get() method raises a DoesNotExist exception
		#So the .get() method returns one model instance or raises an exception.
		category = Category.objects.get(name=category_name)

		#Retrieve all of the associated pages.
		#Note that filter returns >= 1 model instance
		tests = Test.objects.filter(category=category)

		context_dict['tests'] = tests 
		context_dict['category'] = Category
		context_dict['category_name_url'] = category_name

	except Category.DoesNotExist:
	#We get here if we didn't find the specified category
	#Dont' do anything - the template displays the "no category" message for us
		pass

	return render_to_response('torque/category.html', context_dict, context)	

def test(request, test_id):
	#Request our context from the request passed to us
	context = RequestContext(request)
	#Change the underscores in the category name to spaces
	#URLS don't handle spaces well, so we encode them as underscores
	#We can then simply replace the underscores with spaces again to get the name.

	#Create a context dictionary which we can pass to the template rendering engine 
	#We can start by containing the name of thee category passed by the user 
	context_dict = {'test_id': test_id}

	try:
		#Can we find a category with the given name?
		#If we can't, the .get() method raises a DoesNotExist exception
		#So the .get() method returns one model instance or raises an exception.
		test = Test.objects.get(testid=test_id)
		steps = Step.objects.filter(test__testid=test.testid)
		#Retrieve all of the associated pages.
		#Note that filter returns >= 1 model instance
		
		context_dict['test'] = test 
		context_dict['steps'] = steps
		
	except Test.DoesNotExist:
	#We get here if we didn't find the specified category
	#Dont' do anything - the template displays the "no category" message for us
		pass

	return render_to_response('torque/test.html', context_dict, context)

def requirement(request, req_id):
	#Request our context from the request passed to us
	context = RequestContext(request)
	#Change the underscores in the category name to spaces
	#URLS don't handle spaces well, so we encode them as underscores
	#We can then simply replace the underscores with spaces again to get the name.

	#Create a context dictionary which we can pass to the template rendering engine 
	#We can start by containing the name of thee category passed by the user 
	context_dict = {'req_id': req_id}

	try:
		#Can we find a category with the given name?
		#If we can't, the .get() method raises a DoesNotExist exception
		#So the .get() method returns one model instance or raises an exception.
		requirement = Requirement.objects.get(req_id=req_id)
		#Retrieve all of the associated pages.
		#Note that filter returns >= 1 model instance
		
		context_dict['requirement'] = requirement 
		
	except Requirement.DoesNotExist:
	#We get here if we didn't find the specified category
	#Dont' do anything - the template displays the "no category" message for us
		pass

	return render_to_response('torque/requirement.html', context_dict, context)



def add_category(request):

	#Get context from request
	context = RequestContext(request)

	# A HTTP Post?
	if request.method == 'POST':
		form = CategoryForm(request.POST)

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
		form = CategoryForm()

	# Bad form (or form details), no form supplied
	# Render the form with error messages (if any)
	return render_to_response('torque/add_category.html', {'form':form}, context)

def add_test(request):
	context = RequestContext(request)
	
	if request.method == 'POST':
		form = TestForm(request.POST)

		if form.is_valid():
			# This time we cannot commit straight away.
			# Not all fields are automatically populated!
			form.save(commit=True)

			#Retrieve the associated category object so we can add it
			

			return index(request)
		else:
			print form.errors
	else:
		form = TestForm()

	return render_to_response('torque/add_test.html', {'form':form}, context)


def add_requirement(request):
	context = RequestContext(request)
	
	if request.method == 'POST':
		form = RequirementForm(request.POST)

		if form.is_valid():
			# This time we cannot commit straight away.
			# Not all fields are automatically populated!
			form.save(commit=True)

			#Retrieve the associated category object so we can add it
			return index(request)
		else:
			print form.errors
	else:
		form = RequirementForm()

	return render_to_response('torque/add_requirement.html', {'form':form}, context)

def edit_test(request, test_id):
	context = RequestContext(request)
	
	if request.method == 'POST':
		form = TestForm(request.POST)

		if form.is_valid():
			# This time we cannot commit straight away.
			# Not all fields are automatically populated!
			form.save(commit=True)
			#Retrieve the associated category object so we can add it

			return index(request)
		else:
			print form.errors
	else:
		form = TestForm(request.GET)

	return render_to_response('torque/edit_test.html', {'form':form}, context)

def edit_requirement(request, req_id):
	context = RequestContext(request)
	
	if request.method == 'POST':
		form = RequirementForm(request.POST)

		if form.is_valid():
			# This time we cannot commit straight away.
			# Not all fields are automatically populated!
			form.save(commit=True)
			#Retrieve the associated category object so we can add it

			return index(request)
		else:
			print form.errors
	else:
		form = RequirementForm(request.GET)

	return render_to_response('torque/edit_requirement.html', {'form':form}, context)


def register(request):
	if request.session.test_cookie_worked():
		print ">>>> TEST COOKIE WORKED!"
		request.session.delete_test_cookie()

	#Get the request context.
	context = RequestContext(request)

	#boolean value for telling the template whether the registration was successful
	# Set to false initially. Code changes value to True when registration succeeds
	registered = False 

	if request.method == 'POST':
		#attempt to grab user information from the raw information.
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()

			#Now we hash the password with the set_password method
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user 

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			profile.save()

			registered = True
		else:
			print user_form.errors, profile_form.errors 

	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render_to_response(
		'torque/register.html',
		{'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
		context)

def user_login(request):
	context = RequestContext(request)

	if request.method == 'POST':

		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/torque/')
			else:
				return HttpResponse("Your account is disabled.")
		else:
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid login details supplied")

	else:
		return render_to_response('torque/login.html', {}, context)


def search(request):
	context = RequestContext(request)
	result_list = []

	if request.method == 'POST':
		query = request.POST['query'].strip()

		if query:
			result_list = run_query(query)

	return render_to_response('torque/search.html',{'result_list': result_list}, context)



@login_required
def restricted(request):
	return HttpResponse("Can only see this if logged in correctly.")


@login_required
def user_logout(request):
	logout(request)

	return HttpResponseRedirect('/torque/')




