from django.urls import path

from .views import board_game_list, board_game_details

app_name = 'games'
urlpatterns = [
    path('boardgames/', board_game_list, name='list'),
    path('boardgames/<int:id_>', board_game_details, name='details')
]
