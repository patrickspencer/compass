from django.test import TestCase
from django.test import Client

class CoreUrlTestCase(TestCase):
    def test_login_url(self):
        response = c.get('/login/')
        self.assertEqual(response.status_code, 200)
