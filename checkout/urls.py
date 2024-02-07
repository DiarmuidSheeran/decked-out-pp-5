from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
    path('apply_discount/', views.apply_discount, name='apply_discount'),
    path('apply_discount/<str:order_number>/', views.apply_discount_to_order, name='apply_discount_to_order'),
    path('remove_discount/', views.remove_discount, name='remove_discount'),
]