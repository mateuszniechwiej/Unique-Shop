from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.

def products(request):
    """
    A view to display products
    """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """ 
    A view to show single product details
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)
    