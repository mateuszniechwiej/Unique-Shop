from django.test import TestCase


# Create your tests here.
class TestViews(TestCase):
    def test_home_page(self):
        """
        Test home page.
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self. assertTemplateUsed(response, 'home/index.html')
