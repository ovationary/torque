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
