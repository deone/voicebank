from django.test import TestCase
from django.core.urlresolvers import reverse

class ViewsTestCase(TestCase):

    def test_get_contact(self):
	response = self.client.get(reverse('contact'))
	self.assertEqual(response.status_code, 200)
	self.assertTrue('form' in response.context)
	self.assertEqual(response['Content-Type'], "text/html; charset=utf-8")

    def test_post_contact(self):
	data = {
		'name': 'Ola Olu',
		'email': 'alwaysdeone@email.com',
		'phone_number': '08033445566',
		'comment': 'Hi there!'
		}
	response = self.client.post(reverse('contact'), data)
	self.assertEqual(response.status_code, 302)
