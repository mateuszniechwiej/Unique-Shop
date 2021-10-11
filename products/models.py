from django.db import models


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
    has_more_images= models.BooleanField(default=False, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


SIZE_CHOICES = (
    ('small', 'S'),
    ('medium', 'M'),
    ('large', 'L'),
)



class Size(models.Model):
    """
    Model for product price per size variations
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=120, choices=SIZE_CHOICES, default='small')
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.size


COLOURS_CHOICES = (
    ('red', 'RED'),
    ('yellow', 'YELLOW'),
    ('blue', 'BLUE'),
    ('orange', 'ORANGE'),
    ('green', 'GREEN'),
)

class Colour(models.Model):
    """
    Model for product colours
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    colour = models.CharField(max_length=120, choices=COLOURS_CHOICES, default='red')
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.colour







