from django.db import models
from django.conf import settings


# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=20, unique=True)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    post_url = models.TextField()
    code = models.CharField(max_length=40, unique=True)
    discription = models.TextField()
    audience = models.IntegerField()
    watch_grade = models.IntegerField()
    watch_grade_name = models.CharField(max_length=20)
    score = models.FloatField()

    genres = models.ManyToManyField(Genre, related_name='movies')
    

class Review(models.Model):
    content = models.CharField(max_length=100)
    score = models.IntegerField()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    

class Recommend(models.Model):
    title = models.CharField(max_length=40)
    discription = models.TextField()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recommends')
    movies = models.ManyToManyField(Movie, related_name='recommends')
    

class RecommendReview(models.Model):
    content = models.CharField(max_length=100)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recommend_reviews')
    recommend = models.ForeignKey(Recommend, on_delete=models.CASCADE, related_name='recommend_reviews')


class MovieComment(models.Model):
    content = models.TextField()

    recommend = models.ForeignKey(Recommend, on_delete=models.CASCADE, related_name='moviecomments')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='moviecomments')

class Actor(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=40, unique=True)
    image_url = models.TextField()

    movies = models.ManyToManyField(Movie, related_name='actors')


class Director(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=40, unique=True)
    image_url = models.TextField()

    movies = models.ManyToManyField(Movie, related_name='directors')


class CommingMovie(models.Model):
    title = models.CharField(max_length=100)
    openDt = models.DateField()
    post_url = models.TextField()