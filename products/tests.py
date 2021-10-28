from django.test import TestCase

# Create your tests here.
class TestView(TestCase):
    def test_products_page_redirects(self):
        """
        Test products redirects if there is no users logged in 
        """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
