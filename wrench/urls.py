from django.conf.urls import patterns, url 
from wrench import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^new/$', views.add_ticket, name='add_ticket'),
	url(r'^add_ticket/$', views.add_ticket, name='add_ticket'),
	url(r'^view/$', views.show_ticket, name='show_ticket'),
	url(r'^view/(?P<ticket_id>\d+)/$', views.show_single_ticket, name='show_single_ticket'),	
	#url(r'^add_test/$', views.add_test, name='add_test'),
	#url(r'^category/(?P<category_name_url>\w+)/$', views.category, name='category'),
	#url(r'^category/(?P<category_name_url>\w+)/add_test/$', views.add_test, name='add_test'),
	#url(r'^test/(?P<test_id>[-\w]+)/$', views.test, name='test'),
	#url(r'^test/(?P<test_id>[-\w]+)/edit/$', views.edit_test, name='edit_test'),
	#url(r'^register/$', views.register, name='register'),
	#url(r'^login/$', views.user_login, name="login"),
	#url(r'^search/$', views.search, name="search"),
	#url(r'^restricted/$', views.restricted, name='restricted'),
	#url(r'^logout/$', views.user_logout, name='logout'),
	)
