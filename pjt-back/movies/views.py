from django.shortcuts import render, redirect, get_object_or_404
from decouple import config
import requests
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth.decorators import login_required
from .models import Movie, Review, Recommend, Actor, Director, CommingMovie, Genre, RecommendReview, MovieComment


@require_POST
def movieupdate(request):
    pass


