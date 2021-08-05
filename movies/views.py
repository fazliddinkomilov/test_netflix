from builtins import filter
from django.contrib.postgres.search import TrigramSimilarity
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.views import APIView
from movies.models import *
from movies.serializers import *


class MovieViewSet(ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.OrderingFilter]
    ordering_field = ["genre", "-genre"]
    search_fields = ["name"]

    def get_queryset(self):
        queryset = Movie.objects.all()
        query = self.request.query_params.get("search")
        if query is not None:
            queryset = Movie.objects.annotate(similarity=TrigramSimilarity('name', query)
                                              ).filter(similarity__gt=0.4).order_by('-similarity')
        return queryset

    @action(detail=True, methods=['GET'])
    def actors_get(self, request, *args, **kwargs):
        movie = self.get_object()
        serializer = ActorSerializer(movie.actors.all(), many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def add_actor(self, request, pk, *args, **kwargs):
        movie = self.get_object()
        actor_id = request.data["pk"]
        actor = Actor.objects.get(pk=actor_id)
        movie.actors.add(actor)
        movie.save()

        return Response({"status": "Actor added successfully!"})

    @action(detail=True, methods=['POST'])
    def remove_actor(self, request, pk, *args, **kwargs):
        movie = self.get_object()
        actor_id = request.data["pk"]
        actor = Actor.objects.get(pk=actor_id)
        movie.actors.remove(actor)
        movie.save()

        return Response({"status": "Actor removed successfully!"})


class ActorsViewSet(ReadOnlyModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    pagination_class = LimitOffsetPagination


class CommentDetailAPIView(APIView):
    queryset = Comment.objects.all()
    serializers_class = CommentSerializer


class CommentAPI(APIView):
    def get(self, request):
        data = Comment.objects.all()
        serializer = CommentSerializer(data, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)


class CommentDeleteAPI(APIView):

    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        data = self.get_object(pk)
        serializer = CommentSerializer(data)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        data = self.get_object(pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class MovieAPI(APIView):
#     def get(request):
#         movie = Movie.objects.all()
#         serializer = MovieSerializer(movie, many=True)
#         return Response(data=serializer.data)
#
#
# class ActorsAPI(APIView):
#     def get(self, request):
#         actor = Actor.objects.all()
#         serializer = ActorSerializer(actor, many=True)
#         return Response(data=serializer.data)
#
#     def post(self, request):
#         serializer = ActorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(data=serializer.data)

# queryset = Movie.objects.annotate(similarity=TrigramSimilarity("name","Rick and Morty"))
# for movie in queryset:
#    print(movie.name, movie.similarity)
