from django.db import models
from djmoney.models.fields import MoneyField

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
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    has_diff_colors = models.BooleanField(default=False, null=True, blank=True)
    description = models.TextField()
    price = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency='EUR')
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
