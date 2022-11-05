from django.shortcuts import render

from .models import BoardGame


def serialize(object_):
    """Return dict based given objects key that are not private."""
    return {key: value for key, value
            in object_.__dict__.items()
            if not key.startswith('_')}


def home(request):
    """Return response with text greeting."""
    return render(request, 'home.html')


def board_games_list(request):
    """Return response with board games list view."""
    bgs = BoardGame.objects.all()

    return render(request, 'boardgames.html', {'bgs': bgs})
