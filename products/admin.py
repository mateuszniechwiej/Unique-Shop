from django.contrib import admin
from .models import Product, Category, Size, Colour

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    """
    Product admin
    """
    list_display = (
        'sku',
        'name',
        'category',
        'rating',
        'price',
        'image'
    )

    ordering = ('name',) #sorting by name

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Size)
admin.site.register(Colour)