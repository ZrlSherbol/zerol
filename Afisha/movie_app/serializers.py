from rest_framework import serializers
from movie_app.models import Directors, Movie, Review

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title director duration'.split(' ')

class DirectorsSerializer(serializers.ModelSerializer):
    Movie = MovieSerializer()
    class Meta:
        model = Directors
        fields = 'id name movie'.split(' ')

    @property
    def get_movie(self, Directors):
        return Directors.movie.title


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id movie '.split(' ')

class Movie_Review_list_api_view_Sterializater(serializers.ModelSerializer):
    Stars = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = 'id movie stars'.split(' ')

    @property
    def get_stars(self, Review):
        return Review.stars