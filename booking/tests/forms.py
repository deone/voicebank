from django.test import TestCase
from django.contrib.auth.models import User

from booking.forms import BookingForm


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
	self.assertEqual(repr(b), '<Booking: Ade Oluwa>')

    def test_invalid_data(self):
	data = {
		'user': self.user.id,
		'name_on_teller': 'Ade Oluwa',
		'date_of_payment': '02-03-1956',
		'bank_name': 'GTBank'
		}
	form = BookingForm(data)
	self.assertFalse(form.is_valid())
	self.assertEqual(form['date_of_payment'].errors, [u'Enter a valid date.'])
