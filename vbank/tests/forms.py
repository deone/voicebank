from django.test import TestCase
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

from vbank.forms import *

class VoiceClipFormTestCase(TestCase):

    fixtures = ['categories.json']

    def setUp(self):
	self.user = User.objects.create_user('alwaysdeone@yahoo.com',
	'alwaysdeone@yahoo.com', 'test123')
	self.category = Category.objects.get(pk=1)

    def test_invalid_data(self):
	upload_clip = open('/Users/deone/Downloads/BasicLisp1.pdf', 'rb')
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
	upload_clip = open('/Users/deone/Downloads/manifestation.mp3', 'rb')
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
