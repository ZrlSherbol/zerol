from rest_framework import serializers
from movie_app.models import Directors, Movie, Review

class DirectorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Directors
        fields = 'id name'.split(' ')

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title director duration'.split(' ')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id movie'.split(' ')