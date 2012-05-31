from django.test import TestCase
from django.core.urlresolvers import reverse

class ViewsTestCase(TestCase):

    def test_get_events(self):
	response = self.client.get(reverse('events'))
	self.assertEqual(response.status_code, 200)
	self.assertEqual(response['Content-Type'], "text/html; charset=utf-8")
