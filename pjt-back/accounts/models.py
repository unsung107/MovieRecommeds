from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import Movie, Review, Recommend, Actor, Director, CommingMovie, Genre, RecommendReview, MovieComment
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.

class User(AbstractUser):
    
    age = models.IntegerField()
    movies = models.ManyToManyField(, verbose_name=_(""))