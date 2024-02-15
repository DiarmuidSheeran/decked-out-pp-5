from django.shortcuts import render, redirect, reverse
from django.conf import settings
from products.models import Product
from .forms import NewsletterSubscriptionForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.
def send_confirmation_email(email):
    subject = 'Subscription Confirmation'
    html_message = render_to_string('newsletter/confirmation_email.html', {})
    plain_message = strip_tags(html_message) 
    from_email = DEFAULT_FROM_EMAIL
    recipient_list = [email]
    send_mail(subject, plain_message, from_email, recipient_list, html_message=html_message)

def index(request):
    best_sellers = Product.objects.order_by('-productstatistics__total_sold')[:5]
    special_offer_products = Product.objects.filter(is_on_promotion=True, clearance=False)
    clearance_products = Product.objects.filter(clearance=True)
    new_arrival_products = Product.objects.filter(new_arrival=True)

    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            send_confirmation_email(subscription.email)
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



