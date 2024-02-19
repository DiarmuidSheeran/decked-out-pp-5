from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for the view_bag function to render the shopping bag page
    path('', views.view_bag, name='view_bag'),
    # URL pattern for adding items to the shopping bag
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    # URL pattern for adjusting the quantity of items in the shopping bag
    path('adjust/<item_id>/', views.adjust_bag, name='adjust_bag'),
    # URL pattern for removing items from the shopping bag
    path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
]
