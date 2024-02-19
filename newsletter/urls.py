from django.urls import path
from . import views

urlpatterns = [
    # Url to send newsletter emails
    path('send-email/', views.send_newsletter, name='send_email'),
]