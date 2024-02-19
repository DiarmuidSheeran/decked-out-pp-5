from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg


class Category(models.Model):
    """
    Model representing a product category.
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Model representing a product.
    """
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    promotion_price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=1,
        null=False,
        blank=False,
    )
    is_on_promotion = models.BooleanField(default=False)
    clearance = models.BooleanField(default=False)
    new_arrival = models.BooleanField(default=False)
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=0,
        null=True,
        blank=True,
        editable=True
    )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(
        null=True,
        blank=True,
        default='no-product-image.png'
    )
    wishlist = models.ManyToManyField(
        User,
        related_name='wishlist_item',
        blank=True
    )

    def calculate_average_rating(self):
        """
        Calculate the average rating for the product based on its reviews.
        """
        reviews = self.reviews.all()
        if reviews:
            total_rating = sum(review.rating for review in reviews)
            average_rating = total_rating / len(reviews)
            return round(average_rating, 2)
        else:
            return 1

    def update_rating(self):
        """
        Update the rating for the product based on its reviews.
        """
        average_rating = self.reviews.aggregate(Avg('rating'))['rating__avg']
        if average_rating is not None:
            self.rating = round(average_rating, 2)
        else:
            self.rating = 0
        self.save()

    def effective_price(self):
        """
        Get the effective price of the product (taking into account promotion).
        """
        return self.promotion_price if self.is_on_promotion else self.price

    def save(self, *args, **kwargs):
        """
        Override the default save method to set
        SKU and ensure promotion price is not greater than price.
        """
        if not self.sku:
            last_sku = Product.objects.order_by('-sku').first()
            if last_sku:
                last_sku = int(last_sku.sku)
            else:
                last_sku = 0
            self.sku = str(last_sku + 1).zfill(6)

        if self.promotion_price and self.promotion_price > self.price:
            self.promotion_price = self.price

        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductStatistics(models.Model):
    """
    Model representing statistics for a product.
    """
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    total_sold = models.PositiveIntegerField(default=0)
    times_purchased = models.PositiveIntegerField(default=0)
