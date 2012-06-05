from django.test import TestCase
from django.contrib.auth.models import User

from booking.models import Booking

class BookingModelTestCase(TestCase):

    def setUp(self):
	self.user = User.objects.create_user('alwaysdeone@yahoo.com',
		'alwaysdeone@yahoo.com', 'test123')

    def test_success(self):
	b = Booking.objects.create(user=self.user, name_on_teller='Ade Oluwa',
		date_of_payment='2010-03-02', bank_name='GTBank')
	self.assertEqual(repr(b), '<Booking: Ade Oluwa>')
