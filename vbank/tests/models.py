from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User

from vbank.models import *

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


class CategoryModelTestCase(TestCase):

    def setUp(self):
	self.category = Category.objects.get(pk=1)

    def test_get_absolute_url(self):
	response = self.client.get(self.category.get_absolute_url())
	self.assertEqual(response.status_code, 200)
