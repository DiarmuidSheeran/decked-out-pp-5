from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>', views.product_detail, name='product_detail'),
    path('products/<str:sku>/like/', views.wishlist, name='wishlist'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('product-statistics/', views.product_statistics, name='product_statistics'),
    path('admin/products/', views.admin_products, name='admin_products'),
    path('create-discount-code/', views.create_discount_code, name='create_discount_code'),
    path('delete-discount-code/<int:pk>/', views.delete_discount_code, name='delete_discount_code'),
]