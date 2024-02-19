from django import forms
from .models import Review
import crispy_forms
from django.utils.safestring import mark_safe


class ReviewForm(forms.ModelForm):
    """
    Form for creating or updating a product review.
    The form includes fields for rating and comment.
    """
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        exclude = ['reviewer_name']

    rating = forms.ChoiceField(
        choices=[
            (1, '1'),
            (2, '2'),
            (3, '3'),
            (4, '4'),
            (5, '5')
        ],
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    rating.label = mark_safe(
        '<i class="fa-solid fa-star" style="color: #FFD43B;"></i> Star Rating'
    )

    comment = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'rows': '4'}
        ),
        required=True,
    )
    comment.label = mark_safe(
        '<i class="fa-solid fa-comment" \
            style="color: #63E6BE;"></i> Leave a Review'
    )
