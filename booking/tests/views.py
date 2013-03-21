from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from vbank.tests.views import VbankViewsTestCase

class BookingViewsTestCase(VbankViewsTestCase):

    fixtures = ['users.json']

    def setUp(self):
	self.user = User.objects.get(username='alwaysdeone@yahoo.com')

    def test_get_booking(self):
	self.login()
	response = self.client.get(reverse('booking'))
	self.assertEqual(response.status_code, 200)
	self.assertEqual(response['Content-Type'], "text/html; charset=utf-8")
	self.assertTrue('form' in response.context)

    def test_post_booking(self):
	self.login()
	data = {
	    'user': self.user.id,
	    'name_on_teller': 'Ade Oluwa',
	    'date_of_payment': '02/03/1956',
	    'bank_name': 'GTBank'
	    }
	response = self.client.post(reverse('booking'), data)
	self.assertEqual(response.status_code, 302)
