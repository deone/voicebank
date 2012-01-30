from django.test import TestCase
from django.contrib.auth.models import User
from django.core import mail
from django.core.files.uploadedfile import SimpleUploadedFile
from django.conf import settings
from django.core.urlresolvers import reverse

from accounts.forms import *
from accounts.models import *


class UserJoinFormTestCase(TestCase):

    fixtures = ['authtestdata.json']

    def test_user_already_exists(self):
	data = {
		'first_name': 'Ola',
		'last_name': 'Olu',
		'email': 'alwaysdeone@yahoo.com',
		'password': 'test123',
		'gender': 'M',
		'birthday': '02/03/1956'
	    }
	form = UserJoinForm(data)
	self.assertFalse(form.is_valid())
	self.assertEqual(form['email'].errors,
		[u'Email belongs to another user.'])

    def test_invalid_data(self):
	data = {
		'first_name': 'Ola',
		'last_name': 'Olu',
		'email': 'alwaysdeone@gmail.com!',
		'password': 'test123',
		'gender': 'M',
		'birthday': '02/03/1956'
	    }
	form = UserJoinForm(data)
        self.assertFalse(form.is_valid())
        self.assertEquals(form['email'].errors,
                         [u'Enter a valid e-mail address.'])

    def test_email_password(self):
	data = {
		'first_name': 'Ola',
		'last_name': 'Olu',
		'gender': 'F',
		'birthday': '02/03/1956'
	    }
	form = UserJoinForm(data)
	self.assertFalse(form.is_valid())
	self.assertEqual(form['email'].errors,
			[u'This field is required.'])
	self.assertEqual(form['password'].errors,
			[u'This field is required.'])

    def test_success(self):
	data = {
		'first_name': 'Ola',
		'last_name': 'Olu',
		'email': 'earthqiss@yahoo.com',
		'password': 'test123',
		'gender': 'M',
		'birthday': '02/03/1956'
	    }
	form = UserJoinForm(data)
	self.assertTrue(form.is_valid())
	u = form.save()
	self.assertEqual(repr(u), '<User: earthqiss@yahoo.com>')


class UserProfileFormTestCase(TestCase):

    def setUp(self):
	self.user = User.objects.create_user('alwaysdeone@yahoo.com',
	'alwaysdeone@yahoo.com', 'test123')
	Profile.objects.create(user=self.user, birthday='1956-03-02')

    def test_invalid_data(self):
	upload_file = open('/home/deone/Pictures/Me/20110625_003b.jpg', 'rb')
	data = {
		'user': self.user.id,
		'first_name': 'Ola',
		'last_name': 'Olu',
		'about': 'I am Me.',
		'skills': 'Broadcasting, Producing, Directing.',
		'experience': 'I am still me.',
		'phone_number': '080333444556',
		'url_id': 'deone~',
		'location': 'Abuja'
	    }
	file_data = {'photo':
		SimpleUploadedFile(upload_file.name, upload_file.read())}
	form = UserProfileForm(data, file_data)
	self.assertFalse(form.is_valid())
	self.assertEquals(form['phone_number'].errors, [u'Ensure this value has at most 11 characters (it has 12).'])
	self.assertEquals(form['url_id'].errors, [u'Enter a valid value.'])
	
    def test_success(self):
	upload_file = open('/home/deone/Pictures/Me/20110625_003b.jpg', 'rb')
	data = {
		'user': self.user.id,
		'first_name': 'Ola',
		'last_name': 'Olu',
		'about': 'I am Me.',
		'skills': 'Broadcasting, Producing, Directing.',
		'experience': 'I am still me.',
		'phone_number': '08033344455',
		'url_id': 'deone',
		'location': 'Abuja'
	    }
	file_data = {'photo':
		SimpleUploadedFile(upload_file.name, upload_file.read())}
	form = UserProfileForm(data, file_data)
	self.assertTrue(form.is_multipart())
	self.assertTrue(form.is_valid())
	p = form.save()
	self.assertEquals(repr(p), '<Profile: alwaysdeone@yahoo.com>')
	self.assertEquals(p.slug, 'deone')


class ProfileModelTestCase(TestCase):

    def setUp(self):
	self.user = User.objects.create_user('alwaysdeone@yahoo.com',
	'alwaysdeone@yahoo.com', 'test123')

    def test_profile(self):
	upload_file = open('/home/deone/Pictures/Me/20110625_003b.jpg', 'rb')
	p = Profile.objects.create(user=self.user, birthday='1956-03-02',
			slug='alwaysdeone123', gender='F',
			photo=SimpleUploadedFile(upload_file.name,
			    upload_file.read()))
	self.assertEquals(p.user.email, 'alwaysdeone@yahoo.com')
	self.assertEquals(p.slug, 'alwaysdeone123')
	self.assertEquals(p.gender, 'F')
	self.assertEquals(p.birthday, '1956-03-02')
	self.assertEquals(p.skills, '')
	self.assertEquals(p.experience, '')
	self.assertEquals(repr(p), '<Profile: alwaysdeone@yahoo.com>')


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
	self.assertEquals(response.status_code, 302)
	self.assert_(response['Location'].endswith(settings.LOGIN_REDIRECT_URL))

    def test_get_index(self):
	response = self.client.get(reverse('home'))
	self.assertEquals(response.status_code, 200)
	self.assertTrue('categories' in response.context)
	self.assertTrue('clips' in response.context)
	self.assertTrue('events' in response.context)

    def test_get_join(self):
	response = self.client.get(reverse('join'))
	self.assertEquals(response.status_code, 200)
	self.assertTrue('form' in response.context)
	self.assertTrue(response['Content-Type'], 'text/html; charset=utf-8')

    def test_get_profile_edit(self):
	response = self.client.get(reverse('profile_edit'))
	self.assertEquals(response.status_code, 200)
	self.assertTrue('site' in response.context)
	self.assertTrue('form' in response.context)
	self.assertTrue(response['Content-Type'], 'text/html; charset=utf-8')

    def test_post_join(self):
	self.assertEquals(self.join_response.status_code, 302)
	self.assertEquals(len(mail.outbox), 1)
	self.assert_(self.join_response['Location'].endswith(settings.LOGIN_REDIRECT_URL))

    def test_post_profile_edit(self):
	self.login()
	upload_file = open('/home/deone/Pictures/Me/20110625_003b.jpg', 'rb')
	response = self.client.post(reverse('profile_edit'), {
	    'user': self.user.id,
	    'first_name': self.user.first_name,
	    'last_name': self.user.last_name,
	    'about': "It's all about me.",
	    'skills': "Reading.",
	    'experience': "I am still me.",
	    'phone_number': "08033344455",
	    'url_id': self.user.profile.slug,
	    'location': "Abuja",
	    'photo': SimpleUploadedFile(upload_file.name, upload_file.read())
	    })
	self.assertEquals(response.status_code, 200)
