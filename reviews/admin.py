from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'reviewer_name', 'rating', 'created_at')
    list_filter = ('product', 'created_at')
    search_fields = ('reviewer_name', 'comment')
    date_hierarchy = 'created_at'

admin.site.register(Review, ReviewAdmin)
