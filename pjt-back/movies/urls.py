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
    path('api/v1/recommendDetail/<int:recommend_id>/', views.recommendDetail, name='recommendDetail'),
    path('api/v1/movieForUser/<int:user_id>/', views.movieForUser, name='movieForUser'),
    
    path('api/v1/createRecommend/<int:user_id>/', views.createRecommend, name='createRecommend'),
    path('api/v1/deleteRecommend/<int:recommend_id>/', views.deleteRecommend, name='deleteRecommend'),
    path('api/v1/createMovieReview/<int:user_id>/<int:movie_id>/', views.createMovieReview, name='createMovieReview'),
    path('api/v1/deleteRevieReview/<int:review_id>/', views.deleteRevieReview, name='deleteRevieReview'),
    path('api/v1/createRecommendReview/<int:user_id>/<int:recommend_id>/', views.createRecommendReview, name='createRecommendReview'),
    path('api/v1/deleteRecommendReview/<int:review_id>/', views.deleteRecommendReview, name='deleteRecommendReview'),
    path('api/v1/updateMovie/<int:movie_id>/', views.updateMovie, name='updateMovie'),
    path('api/v1/deleteMovie/<int:movie_id>/', views.deleteMovie, name='deleteMovie'),

    path('api/v1/recommendList/<int:user_id>/', views.recommendList, name='recommendList'),

    path('likemovie/<int:movie_id>/<user_id>/', views.likemovie, name='likemovie'),
    path('likedirector/<int:director_id>/<user_id>/', views.likedirector, name='likedirector'),
    path('likeactor/<int:actor_id>/<user_id>/', views.likeactor, name='likeactor'),
    path('likerecommend/<int:recommend_id>/<user_id>/', views.likerecommend, name='likerecommend'),



]
