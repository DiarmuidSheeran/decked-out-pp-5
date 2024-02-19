from django.urls import path
from reviews import views

urlpatterns = [
    # Url path to reviews template
    path(
        'product/<int:product_id>/reviews/',
        views.product_reviews,
        name='product_reviews'
    ),
]
