from django.test import TestCase


# Create your tests here.
class TestViews(TestCase):
    def test_contact_page(self):
        """
        Test contact page
        """
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self. assertTemplateUsed(response, 'contact/contact.html')
