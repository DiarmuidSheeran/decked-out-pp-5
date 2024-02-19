from django import forms


class NewsletterForm(forms.Form):
    """
    Form for composing and sending newsletters.
    """
    subject = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
