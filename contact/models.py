from django.db import models

# https://www.twilio.com/blog/build-contact-form-python-django-twilio-sendgrid add to credits
class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email
