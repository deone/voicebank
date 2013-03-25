from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from events.models import Event

class ModelsTestCase(TestCase):

    def test_success(self):
	upload_file = open('/Users/deone/Downloads/manifestation.jpg', 'rb')
	e = Event.objects.create(title="Voice Training",
		image=SimpleUploadedFile(upload_file.name, upload_file.read()),
		description="Training", venue="Ikeja", date="2001-05-04")
	self.assertEqual(repr(e), '<Event: Voice Training>')
