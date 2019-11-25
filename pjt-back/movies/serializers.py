from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Movie, Genre
User = get_user_model()

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'title', 'discription', 'post_url', 'audience', 'watch_grade_name', )

class GenreSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)

    class Meta:
        model = Genre
        fields = ('name', 'movies', )
        