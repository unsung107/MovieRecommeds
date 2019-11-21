from django.contrib import admin
from .models import Movie, Review, Recommend, Actor, Director, CommingMovie, Genre, RecommendReview, MovieComment

admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Recommend)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(CommingMovie)
admin.site.register(Genre)
admin.site.register(RecommendReview)
admin.site.register(MovieComment)
