from django.conf import settings
from django.shortcuts import get_object_or_404
from unique_shop.settings import DELIVERY_FEE, FREE_DELIVERY
from products.models import Product


def cart_contents(request):
    """
    A view to return all information needed to display the cart
    """
    cart_items = []
    total = 0
    product_count = 0
    grand_total = 0
    # get cart if exitst else creat init empty dict
    cart = request.session.get('cart', {})
    # iretate through all items and tally cost and product count.
    for item_id, quantity in cart.items():
            product = get_object_or_404(Product, pk=item_id)
            for colors, quantity in quantity['items_by_colors'].items():
                total += quantity * product.price
                product_count += quantity
                cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'colors': colors,
                })
    # calc grand total
    if (total < FREE_DELIVERY and total > 0):
        delivery = DELIVERY_FEE
        grand_total = total + delivery
    elif total == 0:
        delivery = 0
        grand_total = 0
    else:
        delivery = 0
        grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': DELIVERY_FEE,
        'free_delivery': FREE_DELIVERY,
        'grand_total': grand_total,
    }

    return context
