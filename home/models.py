from django.db import models


class ContactFormSubmission(models.Model):
    """
    Model representing a submission from a contact form.
    """
    CATEGORY_CHOICES = (
        ('General Inquiry', 'General Inquiry'),
        ('Product Inquiry', 'Product Inquiry'),
        ('Feedback', 'Feedback'),
        ('Other', 'Other'),
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='General Inquiry'
    )
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
