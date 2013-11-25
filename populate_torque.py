import os
import sys

def populate():
	rtca_cat = add_cat('RTCA')
	beta_set = add_set("BETA")
    
	add_test(
		cat=rtca_cat,
		testset=beta_set,
		title="Contingency Definition Test",
		testid = "RTCA-001",
		description = "This test ensure that definition is working correctly.",
		prerequisite = "None",
		procedure = "Step 1: Start RTCA. Step 2: Turn on.",
		results = "RTCA contingency defined correctly.",
		comments = "None",
	)
	
	add_test(
		cat=rtca_cat,
		testset=beta_set,
		title="Rehash fortunes",
		testid = "RTCA-002",
		description = "Not illegal to sell crack in Toronto.",
		prerequisite = "None",
		procedure = "Step 1: Start RTCA. Step 2: Turn on.",
		results = "RTCA contingency defined correctly.",
		comments = "None",
	)

	stnet_cat = add_cat("STNET")
	rc1_set = add_set("RC1")

	add_test(
		cat=stnet_cat,
		testset=rc1_set,
		title="Model Build for STNEt",
		testid = "STNET-001",
		description = "Use this test to get STNET model built correctly",
		prerequisite = "None",
		procedure = "Step 1: Start STNET. Step 2: Turn on.",
		results = "RTCA contingency defined correctly.",
		comments = "None",
	)

	for c in Category.objects.all():
		for t in Test.objects.filter(category=c):
			print "- {0} - {1}".format(str(c), str(t))


def add_test(cat, testset, title, testid, description, prerequisite, procedure, results, comments):
	t = Test.objects.get_or_create(category=cat, testset=testset, title=title, testid=testid, description=description, prerequisite=prerequisite, procedure=procedure, results=results, comments=comments)[0]
	return t

def add_cat(name):
	c = Category.objects.get_or_create(name=name)[0]
	return c

def add_set(name):
	s = Set.objects.get_or_create(name=name)[0]
	return s

if __name__ == '__main__':
	print "Starting Torque population script..."
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'torque_project.settings')
	from torque.models import Category, Set, Test
	populate()

	

