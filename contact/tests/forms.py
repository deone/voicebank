from django.test import TestCase

from contact.forms import ContactForm

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
