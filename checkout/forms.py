from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Form for handling order information.
    """
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }
        # Set autofocus on the first field
        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                # Add placeholders
                self.fields[field].widget.attrs['placeholder'] = placeholder
            # Add custom classes and remove auto-generated labels
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False


class DiscountCodeForm(forms.Form):
    """
    Form for applying discount codes.
    """
    discount_code = forms.CharField(
        label='Promotional Code',
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your discount code here'
        })
    )

    def clean_discount_code(self):
        """
        Clean and normalize discount code input.
        """
        discount_code = self.cleaned_data.get('discount_code')
        if discount_code:
            return discount_code.lower()
        return discount_code
