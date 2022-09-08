from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key' : 'pk_test_51LfgUjGzPQ2aFndOR8PBu7YgToPXb0SUWZASDRupY1coIVjoMgpNd4GiVAb32k8Cl06XA0w67cc5E0ZGzgPydbVE002Lsl6mcT',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)