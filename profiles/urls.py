from django.urls import path
from . import views

urlpatterns = [
    # Url to the profile template
    path(
        '',
        views.profile,
        name='profile'
    ),
    # Url to the order history template
    path(
        'order_history/<order_number>',
        views.order_history,
        name='order_history'
    ),
    # Url to the wishlist template
    path(
        'wishlist',
        views.wishlist,
        name='wishlist'
    ),
    # Url to upload profile picture
    path(
        'upload-profile-picture/',
        views.upload_profile_picture,
        name='upload_profile_picture'
    ),
    # Url to delete account
    path(
        'delete-account/',
        views.delete_account,
        name='delete_account'
    ),
]
