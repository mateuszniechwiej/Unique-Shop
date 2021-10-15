from django.conf import settings
from django.shortcuts import get_object_or_404
from unique_shop.settings import DELIVERY_FEE, FREE_DELIVERY
from products.models import Product

def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    grand_total = 0
    cart = request.session.get('cart', {})

    for item_id, item_qty in cart.items():
        if isinstance(item_qty, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_qty * product.price
            product_count += item_qty
            cart_items.append({
                'item_id': item_id,
                'quantity': item_qty,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for colors, quantity in item_qty['items_by_colors'].items():
                total += quantity * product.price
                product_count += quantity
                cart_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'colors': colors,
                })
                
    if total < FREE_DELIVERY and total != 0:
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