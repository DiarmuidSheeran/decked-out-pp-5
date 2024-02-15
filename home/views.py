from django.shortcuts import render, redirect, reverse
from products.models import Product
from .forms import NewsletterSubscriptionForm

# Create your views here.

def index(request):
    best_sellers = Product.objects.order_by('-productstatistics__total_sold')[:5]
    special_offer_products = Product.objects.filter(is_on_promotion=True, clearance=False)
    clearance_products = Product.objects.filter(clearance=True)
    new_arrival_products = Product.objects.filter(new_arrival=True)

    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    else:
        form = NewsletterSubscriptionForm()

    context = {
        'best_sellers': best_sellers,
        'special_offer_products': special_offer_products,
        'clearance_products': clearance_products,
        'new_arrival_products': new_arrival_products,
        'form': form,
    }

    return render(request, 'home/index.html', context)

