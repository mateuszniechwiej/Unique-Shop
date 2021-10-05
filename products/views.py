from django.shortcuts import render
from .models import Product

# Create your views here.

def display_products(request):
    """
    A view to test displaying products
    """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
    