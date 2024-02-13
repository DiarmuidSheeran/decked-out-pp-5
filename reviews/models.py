from django.db import models
from products.models import Product
from django.contrib.auth.models import User
from checkout.models import Order

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    reviewer_name = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL, default=None)
    rating = models.PositiveIntegerField(default=1)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('reviewer_name', 'product')

    def __str__(self):
        return f"Review for {self.product.name} by {self.reviewer_name}"