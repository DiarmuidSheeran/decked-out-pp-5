from django import forms
from .models import ContactFormSubmission
from newsletter.models import NewsletterSubscription

class NewsletterSubscriptionForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['name','email']

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactFormSubmission
        fields = ['name', 'email', 'category', 'message']

    category = forms.ChoiceField(
        choices=ContactFormSubmission.CATEGORY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )