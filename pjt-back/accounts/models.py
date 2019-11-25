from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie, Review, Recommend, Actor, Director, CommingMovie, Genre, RecommendReview, MovieComment
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.

class User(AbstractUser):
    
    age = models.IntegerField(null=True)
    birthday = models.DateField(default="1993-06-16")

    like_movies = models.ManyToManyField(Movie, related_name="liked_users")
    like_genres = models.ManyToManyField(Genre, related_name="liked_users")
    like_directors = models.ManyToManyField(Director, related_name="liked_users")
    like_actors = models.ManyToManyField(Actor, related_name="liked_users")
    like_commingmovies = models.ManyToManyField(CommingMovie, related_name="liked_users")
    like_recommends = models.ManyToManyField(Recommend, related_name='liked_users')
    like_reviews = models.ManyToManyField(Review, related_name='liked_users')
