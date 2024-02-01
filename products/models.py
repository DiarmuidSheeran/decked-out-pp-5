from django.db import models

# Create your models here.
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    promotion_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    is_on_promotion = models.BooleanField(default=False)
    clearance = models.BooleanField(default=False)
    new_arrival = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.sku:
            last_sku = Product.objects.order_by('-sku').first()
            if last_sku:
                last_sku = int(last_sku.sku)
            else:
                last_sku = 0
            self.sku = str(last_sku + 1).zfill(6)  
        super(Product, self).save(*args, **kwargs)