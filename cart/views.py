from django.shortcuts import redirect, render, reverse

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

    quantity = int(request.POST.get('quantity'))
    # https://stackoverflow.com/questions/5895588/django-multivaluedictkeyerror-error-how-do-i-deal-with-it
    color = request.POST.get('color', False)
    print(color)
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    # checking if item_id == key of cart item 
    if item_id in list(cart.keys()):
        # if the item with that color already in cart then increment qty 
        if color in cart[item_id]['items_by_colors'].keys():
            cart[item_id]['items_by_colors'][color] += quantity
        # else if the item color NOT in the cart set quantity equal to the amount selected to add to cart 
        else:
            cart[item_id]['items_by_colors'][color] = quantity
    #if item not in the cart add item,color and qty to cart 
    else:
        cart[item_id] = {'items_by_colors': {color: quantity}}

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """
    Adjust quantity of each product in the shopping cart
    """
    quantity = int(request.POST.get('quantity'))
    color = request.POST.get('colors')
    cart = request.session.get('cart', {})
    print(color)
    if quantity > 0:
        if item_id in list(cart.keys()):
            if color in cart[item_id]['items_by_colors'].keys():
                cart[item_id]['items_by_colors'][color] = quantity
        else:
            del cart[item_id]['items_by_colors'][color]
            if not cart[item_id]['items_by_colors']:
                cart.pop(item_id)                
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))