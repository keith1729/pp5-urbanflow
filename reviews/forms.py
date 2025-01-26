from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """ Form for submitting a review and rating for a product """

    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.NumberInput(
                attrs={'class': 'form-control rounded-0'}
            ),
            'comment': forms.Textarea(
                attrs={'class': 'form-control rounded-0'}
            ),
        }
