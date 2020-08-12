from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There is nothing in your cart at the moment!")
        return redirect(reverse('books'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HEyVvI9UMljS5mCgqp8lmv7Fa4Mp4NhLx60amKd8tzXLT4iwxf2yPCycAEts2PU9o5ExFYupIJC3k4X43IvMx6X00BavntnKv',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
