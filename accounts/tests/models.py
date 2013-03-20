from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from accounts.models import *

class ProfileModelTestCase(TestCase):

    def setUp(self):
	self.user = User.objects.create_user('alwaysdeone@yahoo.com',
	'alwaysdeone@yahoo.com', 'test123')

	upload_file = open('/Users/deone/Downloads/manifestation.jpg', 'rb')
	self.profile = Profile.objects.create(user=self.user, birthday='1956-03-02',
			slug='alwaysdeone123', gender='F',
			photo=SimpleUploadedFile(upload_file.name,
			    upload_file.read(), 'image/jpeg'))

    def test_profile(self):
	self.assertEqual(self.profile.slug, 'alwaysdeone123')
	self.assertEqual(self.profile.gender, 'F')
	self.assertEqual(self.profile.birthday, '1956-03-02')
	self.assertEqual(self.profile.skills, '')
	self.assertEqual(self.profile.experience, '')
	self.assertEqual(repr(self.profile), '<Profile: alwaysdeone@yahoo.com>')

    def test_get_absolute_url(self):
	response = self.client.get(self.profile.get_absolute_url())
	self.assertEqual(response.status_code, 200)
