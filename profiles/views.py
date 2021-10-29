from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


@login_required
def user_profile(request):
    """
    A view to return the user's profile page.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    template = 'profiles/user_profile.html'
    context = {
        'form': form,
        'profile': profile,
        'orders': orders,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    """
    A view to return user orders history
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This order number {order_number} was already sent.'
    ))
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
