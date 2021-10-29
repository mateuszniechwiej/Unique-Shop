from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'user_full_name': 'Full Name',
            'user_email': 'Email Address',
            'user_phone_number': 'Phone Number',
            'user_postcode': 'Postal Code',
            'user_town_or_city': 'Town or City',
            'user_street_address1': 'Street Address 1',
            'user_street_address2': 'Street Address 2',
            'user_county': 'County, State or Locality',
        }
        # Firld for user profile form
        self.fields['user_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'user_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-dark rounded-0'
            self.fields[field].widget.attrs['aria-label'] = placeholder
            self.fields[field].label = False
