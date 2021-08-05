from django.db import models
from django.contrib.auth import get_user_model
import rest_framework
from datetime import datetime

User = get_user_model()


class Actor(models.Model):
    DEGREES = (
        ("Male", "male"),
        ("Female", "female"),
        ("Different Gender", "different gender")
    )
    name = models.CharField(max_length=100, null=False, blank=False)
    gender = models.CharField(max_length=100, choices=DEGREES)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    year = models.DateField(null=True, blank=True)
    imdb = models.URLField(null=False, blank=False)
    genre = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Actor, related_name='actor', blank=True)
    info = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField(max_length=1300, null=False, blank=False, )
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="comment")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment")
    comment_date = models.DateField(default=datetime.now, blank=True)
