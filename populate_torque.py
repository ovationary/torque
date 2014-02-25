import os
import sys

def populate():

	fep = add_product('FEP','Field Control', '3.5 SP1')
	fep_area1 = add_productarea('Data Acquisition', fep)
	fep_area2 = add_productarea('Controls', fep)
	fep_area3 = add_productarea('Comm Equipmnent Status', fep)
	fep_area4 = add_productarea('Line Switching', fep)
	
	req = add_req(
		req_type="FUNC", 
		author="HEWGILL D.", 
		description="Provide the ability to configure SCADA to let it check that its main threads are not hung and so that it is still responsive.", 
		name="SCADA configuration", 
		sme="SALOMAA OJ", 
		origin="e-terracontrol 3.5 SVPP 2.3.1", 
		productarea=fep_area1,
		)


	fep_cat = add_cat("FEP")
	fep_upgrade_set = add_set("FEP Upgrade")

	add_test(
		cat=fep_cat,
		testset=fep_upgrade_set,
		title="Periodic Scanning",
		testid = "FEP-DATA-001",
		description = "This test ensure that definition is working correctly.",
		prerequisite = "None",
		procedure = "Step 1: Disable CfePerfDriver and Start Process Starter. Step 2: Enable CfePerfDriver.",
		results = "Verify that the gauge in the Statistics View of Scada is increasing.",
		comments = "None",
	)


	add_test(
		cat=fep_cat,
		testset=fep_upgrade_set,
		title="Exception Reporting",
		testid = "FEP-DATA-002",
		description = "The objective of this test is to ensure that an exception processing is performed on telemetered data.",
		prerequisite = "None",
		procedure = "Step 1: Note the display value of the analog or status point. Step 2: Toggle the status point or change the value of the analog.",
		results = "The status or analog point has been updated in the Measurement tabular WebFG Display.",
		comments = "None",
	)
	
	for c in Category.objects.all():
		for t in Test.objects.filter(category=c):
			print "- {0} - {1}".format(str(c), str(t))


def add_product(name, function, version):
	p = Product.objects.get_or_create(name=name, function=function, version=version)[0]
	return p


def add_productarea(name, product):
	pa = ProductArea.objects.get_or_create(name=name, product=product)[0]
	return pa

def add_req(req_type, author, description, name, sme, origin, productarea):
	req = Requirement.objects.get_or_create(req_type=req_type, author=author, description=description, name=name, sme=sme, origin=origin, productarea=productarea)
	return req

def add_cat(name):
	c = Category.objects.get_or_create(name=name)[0]
	return c

def add_set(name):
	s = Set.objects.get_or_create(name=name)[0]
	return s

def add_test(cat, testset, title, testid, description, prerequisite, procedure, results, comments):
	t = Test.objects.get_or_create(category=cat, testset=testset, title=title, testid=testid, description=description, prerequisite=prerequisite, procedure=procedure, results=results, comments=comments)[0]
	return t


if __name__ == '__main__':
	print "Starting Torque population script..."
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'torque_project.settings')
	from torque.models import Category, Set, Test, Product, ProductArea, Requirement
	populate()

	

