from django.test import TestCase
from django.conf import settings
from django.core.urlresolvers import reverse
from django.core import mail
from django.contrib.auth.models import User

class CoreViewsTestCase(TestCase):

    fixtures = ['authtestdata.json']

    def login(self):
	data = {
	    'username': 'alwaysdeone@yahoo.com',
	    'password': 'dayo'
	    }
	response = self.client.post(reverse('login'), data)
	self.assertEqual(response.status_code, 302)
	self.assert_(response['Location'].endswith(settings.LOGIN_REDIRECT_URL))


class VoiceClipsViewTestCase(CoreViewsTestCase):

    def test_get_how(self):
	response = self.client.get(reverse('how'))
	self.assertEqual(response.status_code, 200)

    def test_get_about(self):
	response = self.client.get(reverse('about'))
	self.assertEqual(response.status_code, 200)

    def test_get_voiceclips(self):
	self.login()
	response = self.client.get(reverse('voiceclips'))
	self.assertEqual(response.status_code, 200)

    def test_get_all_clips(self):
	response = self.client.get(reverse('all_clips'))
	self.assertEqual(response.status_code, 200)


class BookingViewTestCase(CoreViewsTestCase):

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
	self.assertEqual(response.status_code, 200)
