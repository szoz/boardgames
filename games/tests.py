from django.test import SimpleTestCase


class BoardGamesListTests(SimpleTestCase):
    """Generic tests for board games pages."""
    databases = {'default'}

    def test_home_page_exists(self):
        """Test if home page exists and returns success status code."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_board_games_list_exists(self):
        """Test if board games list page exists and returns success status code."""
        response = self.client.get('/boardgames/')
        self.assertEqual(response.status_code, 200)
