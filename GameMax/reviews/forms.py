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

        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }

    def clean_rating(self):
        rating = self.cleaned_data['rating']

        if rating < 1 or rating > 5:
            raise forms.ValidationError('Rating must be between 1 and 5.')

        return rating
