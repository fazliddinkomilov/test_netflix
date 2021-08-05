from django.contrib import admin
from movies.models import *


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("name", "gender")
    search_fields = ("name",)
    list_filter = ("gender",)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("name", "year")
    search_fields = ("name",)
    autocomplete_fields = ["actors", "genre"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("text", "user_id", "movie_id")
    search_fields = ("user_id",)
    autocomplete_fields = ["user_id", "movie_id"]
