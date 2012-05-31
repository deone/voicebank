from django.test import TestCase

from contact.models import Contact

class ModelTestCase(TestCase):
    
    def test_success(self):
	c = Contact.objects.create(name='Ade Oluwa',
	email='alwaysdeone@yahoo.com', phone_number='08033445566',
	comment='Keep up the good work!')

	self.assertEqual(repr(c), '<Contact: Ade Oluwa : Keep up the good work!>')
