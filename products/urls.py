from django.urls import path
from . import views

urlpatterns = [
    # Url for products template
    path(
        '',
        views.all_products,
        name='products'
    ),
    # Url for products detail template
    path(
        '<int:product_id>',
        views.product_detail,
        name='product_detail'
    ),
    # Url for adding or removing wishlist items
    path(
        'products/<str:sku>/like/',
        views.wishlist,
        name='wishlist'
    ),
    # Url for adding products to site template
    path(
        'add/',
        views.add_product,
        name='add_product'
    ),
    # Url for editing products template
    path(
        'edit/<int:product_id>/',
        views.edit_product,
        name='edit_product'
    ),
    # Url for deleting products
    path(
        'delete/<int:product_id>/',
        views.delete_product,
        name='delete_product'
    ),
    # Url to product statistics template
    path(
        'product-statistics/',
        views.product_statistics,
        name='product_statistics'
    ),
    # Url to admin products template
    path(
        'admin/products/',
        views.admin_products,
        name='admin_products'
    ),
    # Url path the create discount code template
    path(
        'create-discount-code/',
        views.create_discount_code,
        name='create_discount_code'
    ),
    # Url path to delete discount codes
    path(
        'delete-discount-code/<int:pk>/',
        views.delete_discount_code,
        name='delete_discount_code'
    ),
]
