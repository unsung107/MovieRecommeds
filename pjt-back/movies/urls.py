from django.urls import path
from . import views


app_name = 'movies'
urlpatterns = [
    path('movieupdate/', views.movieupdate, name='movieupdate'),
    path('findmovieupdate/<str:movie_nm>/', views.findmovieupdate, name='findmovieupdate'),
    path('commingmovieupdate/', views.commingmovieupdate, name='commingmovieupdate'),

    path('api/v1/<int:genre_id>/', views.homemovielist, name='homemovielist'),
    path('api/v1/searchNm/<str:movie_nm>/', views.searchMovie, name='searchMovie'),
    path('api/v1/movieDetail/<int:movie_id>/', views.giveMovieInfo, name='giveMovieInfo'),
    path('api/v1/actorDetail/<int:actor_id>/', views.giveActorInfo, name='giveActorInfo'),
    path('api/v1/directorDetail/<int:director_id>/', views.giveDirectorInfo, name='giveDirectorInfo'),
    path('api/v1/userDetail/<int:user_id>/', views.giveUserDetail, name='giveUserDetail'),
    
    path('api/v1/createRecommend/<int:user_id>/', views.createRecommend, name='createRecommend'),

    path('api/v1/recommendList/<int:user_id>/', views.recommendList, name='recommendList'),

]
