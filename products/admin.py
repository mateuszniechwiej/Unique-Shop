from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    """
    Product admin
    """
    list_display = (
        'id',
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