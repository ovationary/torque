from django import forms
from torque.models import Test, Category, Set
from django.contrib.auth.models import User 


class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=128, help_text="Please enter the category name.")
	#views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	#likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

	# An inline class to provide additional information on the form
	class Meta:
		# Provide an association between the ModelForm and a models
		model = Category


class TestForm(forms.ModelForm):
	testid = forms.CharField(max_length=128, help_text="Auto generated Test ID: ")
	category = forms.ModelChoiceField(queryset=Category.objects.all(), help_text="Category: ")
	testset = forms.ModelChoiceField(queryset=Set.objects.all(), help_text="Test Set: ")
	title = forms.CharField(max_length=128, help_text='Title: ')
	description = forms.CharField(max_length=256, help_text='Description: ')
	prerequisite = forms.CharField(max_length=256, help_text='Prerequisite: ')
	procedure = forms.CharField(max_length=256, help_text='Procedure: ')
	results = forms.CharField(max_length=256, help_text='Results:')
	comments = forms.CharField(max_length=256, help_text='Comments: ')

	class Meta:
		model = Test
		fields = ('testid', 'title', 'description', 'category', 'testset', 'prerequisite', 'procedure', 'results', 'comments')


class UserForm(forms.ModelForm):
	username = forms.CharField(help_text="Please enter a username.")
	email = forms.CharField(help_text="Please enter your email.")
	password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a password.")

	class Meta:
		model = User
		fields = ('username','email','password')



