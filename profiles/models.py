from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    User profile model to hold delivery informations
    and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_phone_number = models.CharField(max_length=20, null=True, blank=True)
    user_street_address1 = models.CharField(max_length=80, null=True,
                                            blank=True)
    user_street_address2 = models.CharField(max_length=80, null=True,
                                            blank=True)
    user_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    user_county = models.CharField(max_length=80, null=True, blank=True)
    user_postcode = models.CharField(max_length=20, null=True, blank=True)
    user_country = CountryField(blank_label='Country', null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create new profile or update exisitng profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # for exisitings profile just save profile
    instance.userprofile.save()
