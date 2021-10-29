from django.shortcuts import get_object_or_404, render, redirect,\
                             reverse, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from products.models import Product
from checkout.models import OrderLineItem, Order
from profiles.models import UserProfile
from profiles.forms import UserProfileForm

from .forms import OrderForm
from cart.contexts import cart_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    """
    Checkout data caching
    """
    try:
        # split the client secret to get payment intent id
        pid = request.POST.get('client_secret').split('_secret')[0]
        # set stripe secret key
        stripe.api_key = settings.STRIPE_SECRET_KEY
        # call to modify payment intent and check if user wants to save info
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now.Please try again later. ')
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    A view to return the checkout data
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        # getting items if in the cart else creating empty dict
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        # if form is valid iterate through the cart items
        if order_form.is_valid():
            # commit=False prevents first save
            order = order_form.save(commit=False)
            # split client_secret to get the payment intent ID
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
            for item_id, quantity in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    # Iterate through each color and create a line item
                    for color, quantity in quantity['items_by_colors'].items():
                        order_line_item = OrderLineItem(
                            order=order,
                            quantity=quantity,
                            product=product,
                            color=color,
                        )
                        order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the product in out database wasn't found. "
                        "Please contact us to resolve this issue")
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success',
                                    args=[order.order_number]))
        else:
            messages.error(request, 'There was a problem with your payment form. \
                Please chceck your infnformation.')
    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(request, "Your shopping cart is empty")
            return redirect(reverse('products'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY
        )
        # attempt to prefill the form with profile info
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.user_phone_number,
                    'country': profile.user_country,
                    'postcode': profile.user_postcode,
                    'town_or_city': profile.user_town_or_city,
                    'street_address1': profile.user_street_address1,
                    'street_address2': profile.user_street_address2,
                    'county': profile.user_county,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's information
        if save_info:
            profile_data = {
                'user_phone_number': order.phone_number,
                'user_country': order.country,
                'user_postcode': order.postcode,
                'user_town_or_city': order.town_or_city,
                'user_street_address1': order.street_address1,
                'user_street_address2': order.street_address2,
                'user_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'your order has been successfully completed! \
        Order number: {order_number}. \
        A confirmation email will be sent to {order.email}.')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
