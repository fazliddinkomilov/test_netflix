from django.test import TestCase, Client
import datetime
from movies.models import *


class TestMovieViewSet(TestCase):
    def setUp(self) -> None:
        self.actor = Actor.objects.create(name="Test Actor")
        self.genre = Genre.objects.create(name="Test Genre")
        self.movie = Movie.objects.create(name="Test Movie")
        self.client = Client()

    def test_get_all_movies(self):
        response = self.client.get('/movies/')
        data = response.data

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 1)
        self.assertIsNotNone(data[0]["id"])
        self.assertEquals(data[0]['name'], "Test Movie")

    def test_search(self):
        response = self.client.get('/movies/?search=Test')
        data = response.data

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 1)
        self.assertEquals(data[0]['name'], "Test Movie")

    def test_imdb_order(self):
        response = self.client.get('/movies/?ordering=imdb')
        data = response.data

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(data), 1)
        self.assertEquals(data[0]['name'], "Test Movie")



