from django import forms
from .models import ContactFormSubmission
from newsletter.models import NewsletterSubscription


class NewsletterSubscriptionForm(forms.ModelForm):
    """
    Form for subscribing to the newsletter.
    """
    class Meta:
        model = NewsletterSubscription
        fields = [
            'name',
            'email'
        ]


class ContactForm(forms.ModelForm):
    """
    Form for submitting a contact message.
    """
    class Meta:
        model = ContactFormSubmission
        fields = [
            'name',
            'email',
            'category',
            'message'
        ]

    category = forms.ChoiceField(
        choices=ContactFormSubmission.CATEGORY_CHOICES,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
