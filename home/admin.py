from django.contrib import admin
from .models import ContactFormSubmission

class ContactFormSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'category', 'timestamp')
    list_filter = ('timestamp', 'category')
    search_fields = ('name', 'email', 'message', 'category')
    ordering = ('-timestamp',)

admin.site.register(ContactFormSubmission, ContactFormSubmissionAdmin)