from django.contrib import admin
from .models import Product, Category, ProductStatistics


class ProductAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing products.
    This configuration defines the display fields
    and ordering for the Product model
    in the Django admin interface.
    """
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductStatisticsAdmin(admin.ModelAdmin):
    """
    Admin configuration for managing categories.
    This configuration defines the display fields
    for the Category model
    in the Django admin interface.
    """
    list_display = (
        'product',
        'total_sold',
        'times_purchased',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(
    ProductStatistics,
    ProductStatisticsAdmin
)

