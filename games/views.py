from django.shortcuts import render, get_object_or_404

from .models import BoardGame


def serialize(object_):
    """Return dict based given objects key that are not private."""
    return {key: value for key, value
            in object_.__dict__.items()
            if not key.startswith('_')}


def home(request):
    """Return response with text greeting."""
    return render(request, 'home.html')


def board_game_list(request):
    """Return response with board games list view."""
    bgs = BoardGame.objects.all()

    return render(request, 'boardgame_list.html', {'bgs': bgs})


def board_game_details(request, id_: int):
    """Return page with board game details of given ID."""
    bg = get_object_or_404(BoardGame, id=id_)

    return render(request, 'boardgame_details.html', {'bg': bg})
