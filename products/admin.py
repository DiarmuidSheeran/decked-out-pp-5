from django.contrib import admin
from .models import Product, Category, ProductStatistics

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
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
    list_display = (
        'product',
        'total_sold',
        'times_purchased',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductStatistics, ProductStatisticsAdmin)
