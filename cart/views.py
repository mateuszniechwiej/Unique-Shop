from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.contrib import messages
from products.models import Product


# Create your views here.

def view_cart(request):
    """
    A view to return cart content page
    """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """
    Add quantity of each product to the shopping cart
    """
    product = get_object_or_404(Product, pk=item_id)
    # get qunatity from form and to ineger
    quantity = int(request.POST.get('quantity'))
    # set default value of 'N/A' for color
    color = request.POST.get('color', 'N/A')
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    # checking if item_id == key of cart item
    if item_id in list(cart.keys()):
        # if the item with that color already in cart then increment qty
        if color in cart[item_id]['items_by_colors'].keys():
            cart[item_id]['items_by_colors'][color] += quantity
            messages.success(request,
                             f'{product.name} - colour: {color}.\
                                Quantity updated to\
                                {cart[item_id]["items_by_colors"][color]}')
        # else if the item color NOT in the cart
        else:
            cart[item_id]['items_by_colors'][color] = quantity
            messages.success(request, f'{product.name} - colour:\
                             {color} added to your cart')
    # if item not in the cart
    else:
        cart[item_id] = {'items_by_colors': {color: quantity}}
        messages.success(request, f'{product.name} added to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """
    Adjust quantity of each product in the shopping cart
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    color = request.POST.get('color')
    if quantity > 0:
        if item_id in list(cart.keys()):
            if color in cart[item_id]['items_by_colors'].keys():
                cart[item_id]['items_by_colors'][color] = quantity
                messages.success(request, f'{product.name} added to your cart')
        else:
            del cart[item_id]['items_by_colors'][color]
            if not cart[item_id]['items_by_colors']:
                cart.pop(item_id)
                messages.success(request,
                                 'Product removed from your shopping cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """
    Remove item from cart
    """

    try:
        cart = request.session.get('cart', {})
        color = request.POST.get('color', 'N/A')
        # delete the color key in the items_by_colors
        del cart[item_id]['items_by_colors'][color]
        # if items_by_size empty remove enitre item
        if not cart[item_id]['items_by_colors']:
            cart.pop(item_id)
            messages.success(request,
                             'Product removed from your shopping cart')            

        request.session['cart'] = cart
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing product: {e}')
        return HttpResponse(status=500)
