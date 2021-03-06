from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Movie, Genre, Actor, Director, Recommend, MovieComment, CommingMovie, Review, RecommendReview

User = get_user_model()

class ActorSerializer(serializers.ModelSerializer):
    movies = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all(), many=True)
    liked_users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Actor
        fields = ('id', 'name', 'image_url', 'movies', 'liked_users',)

class DirectorSerializer(serializers.ModelSerializer):
    movies = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all(), many=True)
    liked_users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Director
        fields = ('id', 'name', 'image_url', 'movies', 'liked_users',)

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ('id', 'user', 'score', 'content', )

class RecommendReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RecommendReview
        fields = ('id', 'user', 'content', )

class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    directors = DirectorSerializer(many=True)
    reviews = ReviewSerializer(many=True)
    liked_users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    
    class Meta:
        model = Movie
        fields = ('id', 'title', 'discription', 'post_url', 'audience', 'watch_grade_name', 'actors', 'directors', 'reviews', 'video_url', 'snapshot_url', 'score', 'liked_users', )

class GenreSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)

    class Meta:
        model = Genre
        fields = ('name', 'movies', )
class MovieCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieComment
        fields = ('movie_id', 'recommend_id', 'content', )


class RecommendSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)
    moviecomments = MovieCommentSerializer(many=True)
    recommend_reviews = RecommendReviewSerializer(many=True)
    liked_users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    class Meta:
        model = Recommend
        fields = ('user', 'title', 'discription', 'movies', 'moviecomments', 'id', 'recommend_reviews', 'liked_users',)

class CommingMovieSerializer(serializers.ModelSerializer):
    liked_users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    class Meta:
        model = CommingMovie
        fields = ('title', 'openDt', 'post_url', 'liked_users', )

class UserSerializer(serializers.ModelSerializer):
    like_movies = MovieSerializer(many=True)
    like_genres = GenreSerializer(many=True)
    like_directors = DirectorSerializer(many=True)
    like_actors = ActorSerializer(many=True)
    like_commingmovies = CommingMovieSerializer(many=True)
    like_recommends = RecommendSerializer(many=True)
    recommends = RecommendSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'birthday', 'age', 'like_movies', 'like_genres', 'like_directors', 'like_actors', 'like_commingmovies', 'like_recommends', 'recommends',)
