from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Avg
from products.models import Product
from django.contrib.auth.models import User
from checkout.models import Order


class Review(models.Model):
    """
    Model representing a product review.
    Each review is associated with a product,
    reviewer (user), and optional order.
    It includes a rating and a comment.
    """
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    reviewer_name = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    order = models.ForeignKey(
        Order, null=True,
        on_delete=models.SET_NULL,
        default=None
    )
    rating = models.PositiveIntegerField(default=0)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.product.name} by {self.reviewer_name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.product.update_rating()


@receiver(post_save, sender=Review)
@receiver(post_delete, sender=Review)
def update_product_rating(sender, instance, **kwargs):
    """
    Signal receiver to update the product's
    rating when a review is saved or deleted.
    """
    instance.product.update_rating()
