import uuid
from decimal import Decimal
from django.db import models
from django.db.models import Sum
from django.conf import settings
from django_countries.fields import CountryField
from products.models import Product, ProductStatistics
from profiles.models import UserProfile
from datetime import date


class DiscountCode(models.Model):
    """
    Model to represent discount codes.
    """
    code = models.CharField(max_length=20, unique=True)
    discount_type = models.CharField(
        max_length=10, choices=[('percentage', 'Percentage')]
    )
    discount_amount = models.DecimalField(max_digits=5, decimal_places=2)
    expiration_date = models.DateField()

    def __str__(self):
        return self.code


class Order(models.Model):
    """
    Model to represent orders.
    """
    order_number = models.CharField(
        max_length=32, null=False, editable=False
    )
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
    )
    full_name = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    email = models.EmailField(
        max_length=254,
        null=False,
        blank=False
    )
    phone_number = models.CharField(
        max_length=20,
        null=False,
        blank=False
    )
    country = CountryField(
        blank_label='Country *',
        null=False,
        blank=False
    )
    postcode = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    town_or_city = models.CharField(
        max_length=40,
        null=False,
        blank=False
    )
    street_address1 = models.CharField(
        max_length=80,
        null=False,
        blank=False
    )
    street_address2 = models.CharField(
        max_length=80,
        null=True,
        blank=True
    )
    county = models.CharField(
        max_length=80,
        null=True,
        blank=True
    )
    date = models.DateTimeField(
        auto_now_add=True
    )
    delivery_cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        default=0
    )
    order_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
    )
    grand_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0
    )
    original_bag = models.TextField(
        null=False,
        blank=False,
        default=''
    )
    stripe_pid = models.CharField(
        max_length=254,
        null=False,
        blank=False,
        default=''
    )
    discount_code = models.ForeignKey(
        DiscountCode,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        Calculates order total
        Applies discount code if available
        Updates delivery cost
        Updates grand total
        """
        order_total = Decimal('0.00')

        for line_item in self.lineitems.all():
            product = line_item.product
            if product.is_on_promotion and product.promotion_price:
                order_total += product.promotion_price \
                    * line_item.quantity
            else:
                order_total += product.price * line_item.quantity

        discount_amount = Decimal('0.00')
        if self.discount_code:
            if self.discount_code.discount_type == 'percentage':
                discount_amount = (
                    order_total * self.discount_code.discount_amount
                ) / 100
            else:
                discount_amount = self.discount_code.discount_amount
                discount_amount = min(
                    discount_amount, order_total
                )

        adjusted_order_total = max(
            order_total - discount_amount, Decimal('0.00')
        )

        self.order_total = adjusted_order_total

        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * Decimal(
                settings.STANDARD_DELIVERY_PERCENTAGE
            ) / 100
        else:
            self.delivery_cost = Decimal('0.00')

        self.grand_total = self.order_total + self.delivery_cost

        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to
        set the order number
        if it hasn't been set already.
        Generate order number if not set.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    """
    Model to represent line items in an order.
    """
    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='lineitems'
    )
    product = models.ForeignKey(
        Product, null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField(
        null=False,
        blank=False,
        default=0
    )
    lineitem_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False, blank=False,
        editable=False
    )

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        product = self.product

        if product.is_on_promotion and product.promotion_price:
            self.lineitem_total = product.promotion_price \
                * self.quantity
        else:
            self.lineitem_total = product.price * self.quantity

        product_statistics, _ = ProductStatistics.objects.get_or_create(
            product=self.product
        )
        product_statistics.total_sold += self.quantity
        product_statistics.times_purchased += 1
        product_statistics.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'




