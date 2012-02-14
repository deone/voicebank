from django.test import TestCase
from django.contrib.auth.models import User
from django.core import mail
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from django.core.urlresolvers import reverse

class AccountsViewsTestCase(TestCase):

    def setUp(self):
	data = {
	    'first_name': 'Ola',
	    'last_name': 'Olu',
	    'email': 'earthqiss@yahoo.com',
	    'password': 'test123',
	    'gender': 'M',
	    'birthday': '02/03/1956',
	    }
	self.join_response = self.client.post(reverse('join'), data)
	self.user = User.objects.get(username='earthqiss@yahoo.com')

    def login(self):
	data = {
	    'username': 'earthqiss@yahoo.com',
	    'password': 'test123' 
	    }
	response = self.client.post(reverse('login'), data)
	self.assertEqual(response.status_code, 302)
	self.assert_(response['Location'].endswith(settings.LOGIN_REDIRECT_URL))

    def test_get_index(self):
	response = self.client.get(reverse('home'))
	self.assertEqual(response.status_code, 200)
	self.assertTrue('categories' in response.context)
	self.assertTrue('events' in response.context)
	self.assertTrue('clips' in response.context)
	self.assertEqual([category.pk for category in
	    response.context['categories']], [15, 11, 4, 1, 3, 14, 13,
		6, 7, 9, 8, 5])

    def test_get_join(self):
	response = self.client.get(reverse('join'))
	self.assertEqual(response.status_code, 200)
	self.assertTrue('form' in response.context)
	self.assertTrue(response['Content-Type'], 'text/html; charset=utf-8')

    def test_get_profile_edit(self):
	response = self.client.get(reverse('profile_edit'))
	self.assertEqual(response.status_code, 200)
	self.assertTrue('site' in response.context)
	self.assertTrue('form' in response.context)
	self.assertTrue(response['Content-Type'], 'text/html; charset=utf-8')

    def test_post_join(self):
	self.assertEqual(self.join_response.status_code, 302)
	self.assertEqual(len(mail.outbox), 1)
	self.assert_(self.join_response['Location'].endswith(settings.LOGIN_REDIRECT_URL))

    def test_post_profile_edit(self):
	self.login()
	upload_file = open('/home/deone/Pictures/Me/20110625_003b.jpg', 'rb')
	response = self.client.post(reverse('profile_edit'), {
	    'first_name': self.user.first_name,
	    'last_name': self.user.last_name,
	    'about': "It's all about me.",
	    'skills': "Reading.",
	    'experience': "I am still me.",
	    'phone_number': "08033344455",
	    'url_id': self.user.profile.slug,
	    'location': "Abuja",
	    'photo': SimpleUploadedFile(upload_file.name, upload_file.read(),
	    'image/jpeg')
	    })
	self.assertEqual(response.status_code, 200)
