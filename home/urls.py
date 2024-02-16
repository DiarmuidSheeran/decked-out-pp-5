from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('cookies_policy/', views.cookies_policy, name='cookies_policy'),
    path('returns_policy/', views.returns_policy, name='returns_policy'),
]
