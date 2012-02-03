from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from accounts.models import *

class ProfileModelTestCase(TestCase):

    def setUp(self):
	self.user = User.objects.create_user('alwaysdeone@yahoo.com',
	'alwaysdeone@yahoo.com', 'test123')

    def test_profile(self):
	upload_file = open('/home/deone/Pictures/Me/20110625_003b.jpg', 'rb')
	p = Profile.objects.create(user=self.user, birthday='1956-03-02',
			slug='alwaysdeone123', gender='F',
			photo=SimpleUploadedFile(upload_file.name,
			    upload_file.read(), 'image/jpeg'))
	self.assertEqual(p.user.email, 'alwaysdeone@yahoo.com')
	self.assertEqual(p.slug, 'alwaysdeone123')
	self.assertEqual(p.gender, 'F')
	self.assertEqual(p.birthday, '1956-03-02')
	self.assertEqual(p.skills, '')
	self.assertEqual(p.experience, '')
	self.assertEqual(repr(p), '<Profile: alwaysdeone@yahoo.com>')
