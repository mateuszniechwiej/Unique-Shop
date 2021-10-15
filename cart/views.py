from django.shortcuts import redirect, render

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
    color = request.POST['color']
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        if color in cart[item_id]['items_by_colors'].keys():
            cart[item_id]['items_by_colors'][color] += quantity
        else:
            cart[item_id]['items_by_colors'][color] = quantity
    else:
        cart[item_id] = {'items_by_colors': {color: quantity}}

    request.session['cart'] = cart
    return redirect(redirect_url)