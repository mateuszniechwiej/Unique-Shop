from django.conf import settings

from unique_shop.settings import DELIVERY_FEE

def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    grand_total = 0

    if total < settings.FREE_DELIVERY and total != 0:
        delivery = total + settings.DELIVERY_FEE
        grand_total = delivery + total
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
        'delivery_fee': settings.DELIVERY_FEE,
        'free_delivery': settings.FREE_DELIVERY,
        'grand_total': grand_total,
    }

    return context