from django.forms import ModelForm
from .models import Photo


class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'
