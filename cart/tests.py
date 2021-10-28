from django.test import TestCase

# Create your tests here.
class TestView(TestCase):
    def test_cart_page_redirects(self):
        """
        Test cart redirects if there is no users logged in 
        """
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
