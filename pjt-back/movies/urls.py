from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('movieupdate/', views.movieupdate, name='movieupdate'),
]
