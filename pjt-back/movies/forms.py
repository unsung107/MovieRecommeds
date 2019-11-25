from django import forms
from .models import Recommend

class RecommendCreationForm(forms.ModelForm):

    class Meta:
        model = Recommend
        fields: ('title', 'discription', 'movies', 'user', )