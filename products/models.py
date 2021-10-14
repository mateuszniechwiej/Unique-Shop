from django.db import models
from multiselectfield import MultiSelectField
from django.db import models
from cloudinary.models import CloudinaryField
from django.forms import ModelForm 


class Photo(models.Model):
    image = CloudinaryField('image')


class Category(models.Model):
    """
    Category model
    """

    class Meta:
        verbose_name_plural = "Categories"
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    COLORS_CHOICES = (
    ('red', 'RED'),
    ('yellow', 'YELLOW'),
    ('blue', 'BLUE'),
    ('orange', 'ORANGE'),
    ('green', 'GREEN'),
    ('black','BLACK')
    )

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    colors = MultiSelectField(choices=COLORS_CHOICES, null=True, blank=True)
    size = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = CloudinaryField(
        'image',
        default=''
    )

    def __str__(self):
        return self.name


