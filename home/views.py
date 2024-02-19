from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.contrib import messages
from products.models import Product
from .forms import NewsletterSubscriptionForm, ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import ContactFormSubmission


def send_confirmation_email(email):
    """
    Sends a confirmation email for newsletter subscription.
    """
    subject = 'Subscription Confirmation'
    html_message = render_to_string(
        'newsletter/confirmation_email.html',
        {}
    )
    plain_message = strip_tags(html_message)
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    send_mail(
        subject,
        plain_message,
        from_email,
        recipient_list,
        html_message=html_message
    )


def index(request):
    """
    Renders the index/homepage view.
    Retrieves best-selling, special offer, clearance,
    and new arrival products.
    Handles newsletter subscription form submission.
    """
    best_sellers = Product.objects.order_by(
        '-productstatistics__total_sold'
    )[:5]
    special_offer_products = Product.objects.filter(
        is_on_promotion=True, clearance=False
    )
    clearance_products = Product.objects.filter(
        clearance=True
    )
    new_arrival_products = Product.objects.filter(
        new_arrival=True
    )

    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            subscription = form.save()
            email = form.cleaned_data.get('email')
            send_confirmation_email(subscription.email)
            messages.success(
                request, f'You have successfully \
                    signed up to our newsletter!\n \
                    A confirmation email will be sent to: {email}.'
            )
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


def about_us(request):
    """
    Renders the about us page.
    """
    return render(request, 'home/about_us.html')


def send_feedback_email(email):
    """
    Sends a confirmation email for feedback submission.
    """
    subject = 'Feedback Confirmation Email'
    html_message = render_to_string(
        'home/email/contact_us_email_confirmation.html',
        {}
    )
    plain_message = strip_tags(html_message)
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    send_mail(
        subject,
        plain_message,
        from_email,
        recipient_list,
        html_message=html_message
    )


def contact_us(request):
    """
    Renders the contact us page and handles feedback form submission.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            name = form.cleaned_data.get('name')
            feedback = form.save()
            send_feedback_email(feedback.email)
            messages.success(
                request, f'Your form was successfully processed {name}! \
                We at Decked out thank you for your feedback. \
                A confirmation email will be sent to {email}.'
            )
            return redirect('home')
        else:
            messages.error(
                request,
                'There was an error processing your form. \
                Please check the details and try again.'
            )
    else:
        form = ContactForm()

    context = {
        'form': form
    }

    return render(request, 'home/contact_us.html', context)


def view_contact_form_submissions(request):
    """
    Renders the page displaying contact form submissions.
    """
    submissions = ContactFormSubmission.objects.all()

    context = {
        'submissions': submissions
    }
    return render(request, 'home/contact_form_submissions.html', context)


def cookies_policy(request):
    """
    Renders the cookies policy page.
    """
    return render(request, 'home/cookies_policy.html')


def returns_policy(request):
    """
    Renders the returns policy page.
    """
    return render(request, 'home/returns_policy.html')


