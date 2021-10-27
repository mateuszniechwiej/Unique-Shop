from django.contrib import admin
from .models import Product, Category, Review

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    """
    Product admin
    """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )
    # Sorting by name
    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'product', 'created_date'
    )
    readonly_fields = (
        'created_date',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
