from django.shortcuts import render, redirect, reverse
from .forms import NewsletterForm
from .models import NewsletterSubscription
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def send_newsletter(request):
    """
    View for sending newsletters to subscribers.
    Accessible only to superusers (administrators).
    On successful newsletter submission, redirects to 'profile'.
    On unauthorized access, redirects to 'home' with an error message.
    """
    if not request.user.is_superuser:
        messages.error(
            request,
            'Sorry, only administrators can access this page.'
        )
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            content = form.cleaned_data['content']
            subscribers = NewsletterSubscription.objects.all().values_list(
                'email',
                flat=True
            )
            html_content = render_to_string(
                'newsletter/newsletter_template.html',
                {
                    'subject': subject,
                    'content': content
                }
            )
            send_mail(
                subject,
                content,
                settings.EMAIL_HOST_USER,
                subscribers,
                fail_silently=False
            )
            messages.success(
                request,
                'Newsletter Sent Succesfully'
            )
            return redirect('profile')
        else:
            messages.error(
                request,
                'Failed to send discount code'
            )
    else:
        form = NewsletterForm()

    context = {
        'form': form
    }
    return render(request, 'newsletter/send_email.html', context)

