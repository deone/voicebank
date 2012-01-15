from django.test import TestCase
from django.contrib.auth.models import User
from django.core import mail

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
        self.assertEqual(form['email'].errors,
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


"""class UserProfileFormTestCase(TestCase):

    def test_success(self):
	pass"""


class ProfileModelTestCase(TestCase):

    def setUp(self):
	self.user = User.objects.create_user('alwaysdeone@yahoo.com',
	'alwaysdeone@yahoo.com', 'test123')
    
    def test_profile(self):
	p = Profile.objects.create(user=self.user, birthday='1956-03-02',
			slug='alwaysdeone123', gender='F')
	self.assertEquals(p.user.email, 'alwaysdeone@yahoo.com')
	self.assertEquals(p.slug, 'alwaysdeone123')
	self.assertEquals(p.gender, 'F')
	self.assertEquals(p.birthday, '1956-03-02')
	self.assertEquals(p.skills, '')
	self.assertEquals(p.experience, '')


class JoinViewTest(TestCase):

    fixtures = ['authtestdata.json']

    def test_join(self):
	response = self.client.post('/join', {
	    'first_name': 'Ola',
	    'last_name': 'Olu',
	    'email': 'earthqiss@yahoo.com',
	    'password': 'test123',
	    'gender': 'M',
	    'birthday': '02/03/1956',
	    })
	self.assertEquals(response.status_code, 302)
	self.assertEquals(len(mail.outbox), 1)
