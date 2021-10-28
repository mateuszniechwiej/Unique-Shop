from django.test import TestCase

# Create your tests here.
class TestView(TestCase):
    def test_profiles_page_redirects(self):
        """
        Test checkout profiles redirects if there is no users logged in 
        """
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 302)
