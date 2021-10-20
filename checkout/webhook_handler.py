from django.http import HttpResponse

from .models import Order, OrderLineItem
from products.models import Product

import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle Stripe payment_intent.succeded webhook
        """
        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        #set order not exists
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    # iexact look for exact match but case insensitive
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_cart=cart,
                    stripe_pid=pid
                )
                order_exists = True
                break
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | Success: Order already exists in database',
                    status=200)
            except Order.DoesNotExist:
                attempt +=1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                    content=f'Webhook received: {event["type"]} | Success: Order already exists in database',
                    status=200)
        else:
            order = None
            try:
                for item_id, quantity in json.loads(cart).items():
                    order = Order.objects.create(
                        full_name=shipping_details.email,
                        phone_number=shipping_details.phone,
                        country=shipping_details.address.country,
                        postcode=shipping_details.address.postal_code,
                        town_or_city=shipping_details.address.city,
                        street_address1=shipping_details.address.line1,
                        street_address2=shipping_details.address.line2,
                        county=shipping_details.address.state,
                        original_cart=cart,
                        stripe_pid=pid
                        )
                    product = Product.objects.get(id=item_id)
                    for color, quantity in quantity['items_by_colors'].items():
                        order_line_item = OrderLineItem(
                            order = order,
                            quantity= quantity,
                            product = product,
                            color = color,
                        )
                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(content=f'Webhook received: {event["type"]} | Error: {e}',
                status=500)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | Success: Order created in webhook',
            status=200)


    def handle_payment_intent_payment_failed(self, event):
        """
        Handle Stripe payment_failed webhook
        """
        return HttpResponse(
            content=f'Webhook received {event["type"]}',
            status=200)
