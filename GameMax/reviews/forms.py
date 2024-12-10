from django import forms

from GameMax.reviews.models import Review


class EditReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review_text']

        labels = {
            'rating': '',
            'review_text': ''
        }