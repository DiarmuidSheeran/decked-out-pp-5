from django.contrib import admin
from .models import UserProfile

# Registers the users profile in the admin
admin.site.register(UserProfile)
