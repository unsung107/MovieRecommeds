from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Movie, Genre, Actor, Director
User = get_user_model()

class ActorSerializer(serializers.ModelSerializer):
    movies = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all(), many=True)

    class Meta:
        model = Actor
        fields = ('id', 'name', 'image_url', 'movies',)

class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    class Meta:
        model = Movie
        fields = ('id', 'title', 'discription', 'post_url', 'audience', 'watch_grade_name', 'actors', )

class GenreSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)

    class Meta:
        model = Genre
        fields = ('name', 'movies', )



        