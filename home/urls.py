from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Home page
    path(
        '',
        views.index,
        name='home'
    ),
    # About us page
    path(
        'about_us/',
        views.about_us,
        name='about_us'
    ),
    # Contact us page
    path(
        'contact_us/',
        views.contact_us,
        name='contact_us'
    ),
    # Cookies policy page
    path(
        'cookies_policy/',
        views.cookies_policy,
        name='cookies_policy'
    ),
    # Returns policy page
    path(
        'returns_policy/',
        views.returns_policy,
        name='returns_policy'
    ),
    # View contact form submissions page
    path(
        'contact-form-submissions/',
        views.view_contact_form_submissions,
        name='view_contact_form_submissions'
    ),
]

