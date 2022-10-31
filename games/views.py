from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import BoardGame


def serialize(object_):
    """Return dict based given objects key that are not private."""
    return {key: value for key, value
            in object_.__dict__.items()
            if not key.startswith('_')}


def home(request):
    """Return response with text greeting."""
    return HttpResponse('Hello to BoardGames')


def board_games_list(request):
    """Return response with board games list view."""
    payload = [serialize(bg) for bg in BoardGame.objects.all()]

    return JsonResponse(payload, safe=False)
