from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User

from core.models import *

class VoiceClipModelTestCase(TestCase):

    fixtures = ['categorytestdata.json']
    
    def setUp(self):
	self.user = User.objects.create_user('alwaysdeone@yahoo.com',
	'alwaysdeone@yahoo.com', 'test123')
	self.category = Category.objects.all()[0]

    def test_success(self):
	upload_clip = open('/home/deone/Downloads/Sugarr-IYAWO_LO.mp3', 'rb')
	v = VoiceClip.objects.create(user=self.user, name="Be mine",
		voice_clip=SimpleUploadedFile(upload_clip.name,
		    upload_clip.read()), language='English',
		    date_added='2011-05-04', is_active=True,
		    category=self.category)
	self.assertEqual(repr(v), '<VoiceClip: Be mine by >')


class ContactModelTestCase(TestCase):
    
    def test_success(self):
	c = Contact.objects.create(name='Ade Oluwa',
	email='alwaysdeone@yahoo.com', phone_number='08033445566',
	comment='Keep up the good work!')

	self.assertEqual(repr(c), '<Contact: Ade Oluwa : Keep up the good work!>')


class BookingModelTestCase(TestCase):

    def setUp(self):
	self.user = User.objects.create_user('alwaysdeone@yahoo.com',
		'alwaysdeone@yahoo.com', 'test123')

    def test_success(self):
	b = Booking.objects.create(user=self.user, name_on_teller='Ade Oluwa',
		date_of_payment='2010-03-02', bank_name='GTBank')
	self.assertEqual(repr(b), '<Booking: Ade Oluwa>')


class CategoryModelTestCase(TestCase):

    def setUp(self):
	self.category = Category.objects.get(pk=1)

    def test_get_absolute_url(self):
	response = self.client.get(self.category.get_absolute_url())
	self.assertEqual(response.status_code, 200)
