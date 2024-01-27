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
        'stripe_public_key': 'pk_test_51OS5DgEPBBYTB9R1ljMgfHt54Hj8cQkwCkDDhKXws2iMY2OeE0uDI7BB7OUFM1EpCDHfLqOa2JfDW5dTUWA5so4N00Z9twi4oU',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)