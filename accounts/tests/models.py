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
	self.assertEquals(p.user.email, 'alwaysdeone@yahoo.com')
	self.assertEquals(p.slug, 'alwaysdeone123')
	self.assertEquals(p.gender, 'F')
	self.assertEquals(p.birthday, '1956-03-02')
	self.assertEquals(p.skills, '')
	self.assertEquals(p.experience, '')
	self.assertEquals(repr(p), '<Profile: alwaysdeone@yahoo.com>')
