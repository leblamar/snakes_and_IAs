from django.urls import path
from . import views

app_name = "tictactoe"
urlpatterns = [
    path("", views.index_view, name="index"),
    path("new_game/", views.new_game, name="new_game"),
]