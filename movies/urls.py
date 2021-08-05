from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("movies", MovieViewSet)
router.register("actors", ActorsViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("comments/", CommentAPI.as_view(), name="comments"),
    path('comments/<int:pk>/', CommentDeleteAPI.as_view()),
    # path("movies/", MovieAPI.as_view(), name="movies"),
    # path("actors/", ActorsAPI.as_view(), name="actors")
]
