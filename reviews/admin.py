from django.contrib import admin
from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Review model.
    Displays fields in the list view,
    filters by product and created_at date,
    enables searching by reviewer_name and comment,
    and adds a date hierarchy.
    """
    list_display = ('product', 'reviewer_name', 'rating', 'created_at')
    list_filter = ('product', 'created_at')
    search_fields = ('reviewer_name', 'comment')
    date_hierarchy = 'created_at'


admin.site.register(Review, ReviewAdmin)
