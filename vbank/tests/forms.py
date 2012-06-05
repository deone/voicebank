from django.test import TestCase
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

from vbank.forms import *

class VoiceClipFormTestCase(TestCase):

    def setUp(self):
	self.user = User.objects.create_user('alwaysdeone@yahoo.com',
	'alwaysdeone@yahoo.com', 'test123')
	self.category = Category.objects.all()[0]

    def test_invalid_data(self):
	upload_clip = open('/home/deone/Downloads/printable_final.pdf', 'rb')
	data = {
		'user': self.user.id,
		'name': 'Be My Man',
		'language': 'English',
		'category': self.category.id
		}
	file_data = {'voice_clip': SimpleUploadedFile(upload_clip.name,
	    upload_clip.read(), 'application/pdf')}
	form = VoiceClipForm(data, file_data)
	self.assertFalse(form.is_valid())
	self.assertEqual(form['voice_clip'].errors, [u"Please upload an mp3 audio file."])
    
    def test_success(self):
	upload_clip = open('/home/deone/Downloads/Sugarr-IYAWO_LO.mp3', 'rb')
	data = {
		'user': self.user.id,
		'name': 'Be My Man',
		'language': 'English',
		'category': self.category.id
		}
	file_data = {'voice_clip': SimpleUploadedFile(upload_clip.name,
	    upload_clip.read(), 'audio/mpeg')}
	form = VoiceClipForm(data, file_data)
	self.assertTrue(form.is_multipart())
	self.assertTrue(form.is_valid())
	vc = form.save()
	self.assertEqual(repr(vc), '<VoiceClip: Be My Man by >')


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
	self.assertEqual(repr(c), '<Contact: Ade Oluwa : Keep up the good work!>')

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
