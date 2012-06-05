from django.test import TestCase
from django.conf import settings
from django.core.urlresolvers import reverse
from django.core import mail
from django.contrib.auth.models import User

class VbankViewsTestCase(TestCase):

    fixtures = ['authtestdata.json']

    def login(self):
	data = {
	    'username': 'alwaysdeone@yahoo.com',
	    'password': 'dayo'
	    }
	response = self.client.post(reverse('login'), data)
	self.assertEqual(response.status_code, 302)
	self.assert_(response['Location'].endswith(settings.LOGIN_REDIRECT_URL))


class VoiceClipsViewTestCase(VbankViewsTestCase):

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
