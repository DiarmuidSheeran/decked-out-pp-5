from django import forms
from .models import Product, Category
from .widgets import CustomClearableFileInput
from checkout.models import DiscountCode


class ProductForm(forms.ModelForm):
    """
    Form for adding or editing a product.
    This form allows users to add or edit product
    details such as name, description, price, category,
    promotion status, image, etc. The image field
    is customized using CustomClearableFileInput widget,
    and the category field choices are
    populated with friendly names.
    """
    class Meta:
        model = Product
        exclude = ('wishlist',)

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [
            (c.id, c.get_friendly_name()) for c in categories
        ]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class DiscountCodeForm(forms.ModelForm):
    """
    Form for adding or editing a discount code.
    This form allows users to add or edit
    discount code details such as code, discount type,
    discount amount, and expiration date.
    The expiration date field is customized to use a date picker.
    """
    class Meta:
        model = DiscountCode
        fields = [
            'code',
            'discount_type',
            'discount_amount',
            'expiration_date'
        ]
        widgets = {
            'expiration_date': forms.DateInput(attrs={'type': 'date'})
        }
