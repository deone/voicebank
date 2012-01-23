from django.test import TestCase
from django.contrib.auth.models import User
from django.core import mail

from core.models import *
from core.forms import *


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
	b = form.save()
	self.assertEquals(repr(b), '<Profile: alwaysdeone@yahoo.com>')
