from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('upload-profile-picture/', views.upload_profile_picture, name='upload_profile_picture'),
]