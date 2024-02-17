from django import forms
from .models import Product, Category
from .widgets import CustomClearableFileInput
from checkout.models import DiscountCode


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('wishlist',)

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

class DiscountCodeForm(forms.ModelForm):
    class Meta:
        model = DiscountCode
        fields = ['code', 'discount_type', 'discount_amount', 'expiration_date']
        widgets = {
            'expiration_date': forms.DateInput(attrs={'type': 'date'})
        }