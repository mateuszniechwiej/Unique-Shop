from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "Your shopping cart is empty")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JlxhHBdOsb29ESmtf5eDVHLFBDzDSKwN9F5rwzWWekzTnWpHuadIzD1QXHvVYReTAs4rxj0oL1TmPNZH3V2aBBL00OCvhGMCy', 
        'client_secret': 'testing client secret',  
    }

    return render(request, template, context)
