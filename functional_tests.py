from selenium import webdriver
import unittest


'''
1. Incident Report

A dark stormy night for ORMS. 100,000 customers out of power, and the ORMS Application starts to hiccup. Dispatcher logs onto
Choreo and is presented with a simple view for the Customer Support portal. Incident Manager just crashed on her, so she needs to 
submit a ticket. She clicks on the "Create New Ticket" button.

As the team lead for the ORMS App Support team, Scott logs onto Choreo the first thing in the morning. He's presented with a browser window
and a Dashboard presenting a visual health status of the ORMS Production Environment, the RFCS for the Day, and the Customer Support portal.

2. Triage

Scott sees that there's a new Customer Ticket opened on the weekend, complaining about Autodialer issues. He clicks on the ticket URL,
and he's taken to a view that presents a chronological history of the ticket item. He can scroll to see when the ticket was logged, 
who logged the ticket, and what the current status is. Scott sees that the ASM team has added an update, and forwarded the request to the 
Infrastructure team. 

3. Change Management

John's the DOMC Manager, and he's having a rough day. A Level 3 storm is passing through Central Ontario and about 100,000 customers
are at risk of being without power. ORMS Grouping Manager seems to be exceptionally slow, and its after hours. John logs onto his mobile 
Choreo app, and submits a support request using the form provided. The support ticket triggers an email to OGCC SCE, as well as 
an SMS notification to the on call staff. 

4. Knowledge Management


'''

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser  = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_login(self):
		self.browser.get('http://localhost:8000')

		self.assert('To-do', self.browser.title)
		self.fail('Finish the test!')


if __name__ == '__main__':
	unittest.main(warnings='ignore')

Incident Management

--Next --
# Ability to capture the orginator's contact information
# Ability to assign a priority ranking to a ticket
# Ability to assign a categorization to a ticket
# Abiliy to capture certain mandatory details
# Ability to enforce field validation
# Ability to capture a summary field for use by listing screens and a detailed field for fully explaninning the incident
# Ability to assign an incident ticket to an invidivual or a team
# Ability to capture related incident number
# Ability to notify a team or individual when they've been assigned a ticket
# Ability to create a change request within the incident ticket



- Future --
# Ability to create incident ticket from email
# Ability to create an incident from monitoring alert
# Ability to share a ticket
# Ability of the system to change the status of a ticket as it progresses towards resolution
# Ability to auto create child tickets when there is a parent/child relationship
# Ability for the system to resolve any child or related tickets whent the highest level ticket has been resolved
# Ability to add attachment to a ticket
# Ability to display ticket status on all listing screens through the various incident management stages
# Ability for the high priority incidents to auto generate information status messages at specific intervals
# Ability to clearly differentiate those incidents to which a Service level Agreement appies
# Ability to capture solution details
# Abiltiy to put an incident on hold. Will stop the clock for all SLA calculations
# Ability to create a problem ticket from the incident ticket, cpaturing all relevant information
# Ability to hide specific fields from orginator or 3rd party vendor
# Ability to advise originator that a ticket has been resolved
# Ability to change ticket status from resolved backt o active status
# Abiltiy to assign a ticket to a 3rd party vendor
# Ability to restrict visibility of an incident

