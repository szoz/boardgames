from django.test import TestCase

from .models import BoardGame


class HomeTests(TestCase):
    """Home page test."""

    def test_exists_and_content(self):
        """Test if home page is available and returns valid content."""
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome')


class BoardGamesListTests(TestCase):
    """Board games list tests."""

    def test_exists(self):
        """Test if URL is valid."""
        response = self.client.get('/boardgames/')

        self.assertEqual(response.status_code, 200)

    def test_lists_board_games(self):
        """Test if response contains a table and BoardGames attribute values."""
        bg1 = {'id': 1,
               'name': 'Splendor',
               'year': 2000,
               'description': 'A very splendid game'}
        bg2 = {'id': 2,
               'name': 'Terra Nova',
               'year': 2023,
               'description': 'A new TM-based game'}

        BoardGame.objects.create(**bg1)
        BoardGame.objects.create(**bg2)
        response = self.client.get('/boardgames/')

        self.assertContains(response, '<table')
        self.assertContains(response, '<tr')
        self.assertContains(response, bg1['name'])
        self.assertContains(response, bg1['description'])
        self.assertContains(response, bg2['name'])
        self.assertContains(response, bg2['description'])
