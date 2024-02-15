from django.shortcuts import render
from products.models import Product
# Create your views here.

def index(request):
    best_sellers = Product.objects.order_by('-productstatistics__total_sold')[:5]
    special_offer_products = Product.objects.filter(is_on_promotion=True, clearance=False)
    clearance_products = Product.objects.filter(clearance=True)
    new_arrival_products = Product.objects.filter(new_arrival=True)

    context = {
        'best_sellers': best_sellers,
        'special_offer_products': special_offer_products,
        'clearance_products': clearance_products,
        'new_arrival_products': new_arrival_products,
    }

    return render(request, 'home/index.html', context)

