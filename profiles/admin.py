from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'user_phone_number',
    'user_street_address1',
    'user_street_address2',
    'user_town_or_city',
    'user_county',
    'user_postcode',
    'user_country',
    )

admin.site.register(UserProfile, UserProfileAdmin)