from django.test import TestCase

from .models import BoardGame


class HomeTests(TestCase):
    """Home page test."""

    def test_exists_and_content(self):
        """Test if home page is available and returns valid content."""
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome')


class BoardGameListTests(TestCase):
    """Board games list tests."""
    bg1 = {'id': 1,
           'name': 'Splendor',
           'year': 2000,
           'description': 'A very splendid game'}
    bg2 = {'id': 2,
           'name': 'Terra Nova',
           'year': 2023,
           'description': 'A new TM-based game'}

    def setUp(self):
        """Create boardgames objects for specific tests."""
        BoardGame.objects.create(**self.bg1)
        BoardGame.objects.create(**self.bg2)

    def test_exists(self):
        """Test if URL is valid."""
        response = self.client.get('/boardgames/')

        self.assertEqual(response.status_code, 200)

    def test_board_game_list(self):
        """Test if response contains a table and BoardGames attribute values."""
        response = self.client.get('/boardgames/')

        self.assertContains(response, '<table')
        self.assertContains(response, '<tr')
        self.assertContains(response, self.bg1['name'])
        self.assertContains(response, self.bg1['description'])
        self.assertContains(response, self.bg2['name'])
        self.assertContains(response, self.bg2['description'])

    def test_board_game_details_url(self):
        """Test if board games list contains URLs to details view."""
        response = self.client.get('/boardgames/')

        self.assertContains(response, f'<a href="/boardgames/{self.bg1["id"]}"')
        self.assertContains(response, f'<a href="/boardgames/{self.bg2["id"]}"')


class BoardGameDetailsTests(TestCase):
    """Board games list tests."""
    bg = {'id': 1,
          'name': 'Splendor',
          'year': 2000,
          'description': 'A very splendid game'}

    def setUp(self):
        """Create boardgames objects for specific tests."""
        BoardGame.objects.create(**self.bg)

    def test_exists(self):
        """Test if URL is valid."""
        response_valid = self.client.get('/boardgames/1')
        response_invalid = self.client.get('/boardgames/2')

        self.assertEqual(response_valid.status_code, 200)
        self.assertEqual(response_invalid.status_code, 404)

    def test_board_game_details(self):
        """Test if response contains a card with Boardgames' attributes."""
        response = self.client.get('/boardgames/1')

        self.assertContains(response, self.bg['name'])
        self.assertContains(response, self.bg['year'])
        self.assertContains(response, self.bg['description'])
