from django import forms

class NewsletterForm(forms.Form):
    subject = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)