from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from checkout.models import DiscountCode


def bag_contents(request):
    """
    A context processor to provide bag-related information to templates.
    This function calculates the total cost, product count, delivery charge,
    and discount amount for items in the shopping bag.
    Returns:
        A dictionary containing bag-related information
        to be added to the context.
    """
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    discount_code_id = request.session.get('discount_code_id', None)
    discount_amount = 0

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        item_price = product.price

        if product.is_on_promotion and product.promotion_price is not None:
            item_price = product.promotion_price

        total += quantity * item_price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'item_price': item_price
        })

    if discount_code_id:
        try:
            discount_code = DiscountCode.objects.get(id=discount_code_id)
            discount_code.discount_type == 'percentage'
            discount_amount = (total * discount_code.discount_amount) / 100
            discount_amount = min(discount_amount, total)
        except DiscountCode.DoesNotExist:
            discount_amount = 0
    total = max(0, total - discount_amount)

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
        'discount_amount': discount_amount,
    }

    return context
