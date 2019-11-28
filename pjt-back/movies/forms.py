from django import forms
from .models import Recommend, Review, RecommendReview, Movie

class RecommendCreationForm(forms.ModelForm):

    class Meta:
        model = Recommend
        fields = ('title', 'discription', 'movies', 'user', )

class ReviewCreationForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('content', 'score', )

class RecommendReviewCreationForm(forms.ModelForm):

    class Meta:
        model = RecommendReview
        fields = ('content', )
