from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from movies.models import *
import datetime


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "name", "gender")

    # def validate(self, data):
    #     if data['birthdate'] < datetime.date(1950, 1, 1):
    #         raise serializers.ValidationError(detail="fuck, how the hell is he alive?")
    #     return data


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = ("id", "name", "year", "imdb", "genre", "actors")


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ("id", "text", "user_id", "movie_id")
