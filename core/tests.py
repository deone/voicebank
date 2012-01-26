from django.test import TestCase
from django.contrib.auth.models import User
from django.core import mail
from django.conf import settings
from django.core.urlresolvers import reverse

from core.models import *
from core.forms import *


class ContactModelTestCase(TestCase):
    
    def test_success(self):
	c = Contact.objects.create(name='Ade Oluwa',
	email='alwaysdeone@yahoo.com', phone_number='08033445566',
	comment='Keep up the good work!')

	self.assertEquals(repr(c), '<Contact: Ade Oluwa : Keep up the good work!>')


class ContactFormTestCase(TestCase):
    
    def test_success(self):
	data = {
		'name': 'Ade Oluwa',
		'email': 'alwaysdeone@yahoo.com',
		'phone_number': '08033445566',
		'comment': 'Keep up the good work!'
		}
	form = ContactForm(data)
	self.assertTrue(form.is_valid())
	c = form.save()
	self.assertEquals(repr(c), '<Contact: Ade Oluwa : Keep up the good work!>')

    def test_invalid_data(self):
	data = {
		'name': 'Ade Oluwa',
		'email': 'alwaysdeone@yahoo.com!',
		'phone_number': '08033445566',
		'comment': 'Keep up the good work!'
		}
	form = ContactForm(data)
	self.assertFalse(form.is_valid())
	self.assertTrue(form['email'].errors, [u'Enter a valid e-mail address.'])


class ContactViewTestCase(TestCase):

    def test_get_contact(self):
	response = self.client.get(reverse('contact'))
	self.assertEquals(response.status_code, 200)
	self.assertTrue('form' in response.context)
	self.assertEquals(response['Content-Type'], "text/html; charset=utf-8")

    def test_post_contact(self):
	data = {
		'name': 'Ola Olu',
		'email': 'alwaysdeone@email.com',
		'phone_number': '08033445566',
		'comment': 'Hi there!'
		}
	response = self.client.post(reverse('contact'), data)
	self.assertEquals(response.status_code, 200)


class BookingModelTestCase(TestCase):

    def setUp(self):
	self.user = User.objects.create_user('alwaysdeone@yahoo.com',
		'alwaysdeone@yahoo.com', 'test123')

    def test_success(self):
	b = Booking.objects.create(user=self.user, name_on_teller='Ade Oluwa',
		date_of_payment='2010-03-02', bank_name='GTBank')
	self.assertEquals(repr(b), '<Booking: Ade Oluwa>')


class BookingFormTestCase(TestCase):

    def setUp(self):
	self.user = User.objects.create_user('alwaysdeone@yahoo.com',
		'alwaysdeone@yahoo.com', 'test123')

    def test_success(self):
	data = {
		'user': self.user.id,
		'name_on_teller': 'Ade Oluwa',
		'date_of_payment': '02/03/1956',
		'bank_name': 'GTBank'
		}
	form = BookingForm(data)
	self.assertTrue(form.is_valid())
	b = form.save()
	self.assertEquals(repr(b), '<Booking: Ade Oluwa>')

    def test_invalid_data(self):
	data = {
		'user': self.user.id,
		'name_on_teller': 'Ade Oluwa',
		'date_of_payment': '02-03-1956',
		'bank_name': 'GTBank'
		}
	form = BookingForm(data)
	self.assertFalse(form.is_valid())
	self.assertEquals(form['date_of_payment'].errors, [u'Enter a valid date.'])


class BookingViewTestCase(TestCase):

    fixtures = ['authtestdata.json']

    def setUp(self):
	self.user = User.objects.get(username='alwaysdeone@yahoo.com')

    def login(self):
	data = {
	    'username': 'alwaysdeone@yahoo.com',
	    'password': 'dayo'
	    }
	response = self.client.post(reverse('login'), data)
	self.assertEquals(response.status_code, 302)
	self.assert_(response['Location'].endswith(settings.LOGIN_REDIRECT_URL))

    def test_get_booking(self):
	self.login()
	response = self.client.get(reverse('booking'))
	self.assertEquals(response.status_code, 200)
	self.assertEquals(response['Content-Type'], "text/html; charset=utf-8")
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
	self.assertEquals(response.status_code, 200) 
