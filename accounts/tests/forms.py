from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from accounts.forms import *


class UserJoinFormTestCase(TestCase):

    fixtures = ['authtestdata.json']

    def test_user_already_exists(self):
	data = {
		'first_name': 'Ola',
		'last_name': 'Olu',
		'email': 'alwaysdeone@yahoo.com',
		'password': 'test123',
		'gender': 'M',
		'birthday': '26/03/1956'
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
		'birthday': '26/03/1956'
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
		'birthday': '26/03/1956'
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
		'birthday': '26/03/1956'
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
		'slug': 'deone~',
		'location': 'Abuja'
	    }
	file_data = {'photo':
		SimpleUploadedFile(upload_file.name, upload_file.read(),
		'image/jpeg')}
	form = UserProfileForm(data, file_data)
	self.assertFalse(form.is_valid())
	self.assertEqual(form['phone_number'].errors, [u'Ensure this value has at most 11 characters (it has 12).'])
	self.assertEqual(form['slug'].errors, [u'Enter a valid value.'])
	
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
		'slug': 'deone',
		'location': 'Abuja'
	    }
	file_data = {'photo':
		SimpleUploadedFile(upload_file.name, upload_file.read(),
		'image/jpeg')}
	form = UserProfileForm(data, file_data)
	self.assertTrue(form.is_multipart())
	self.assertTrue(form.is_valid())
	p = form.save()
	self.assertEqual(repr(p), '<Profile: alwaysdeone@yahoo.com>')
	self.assertEqual(p.slug, 'deone')
