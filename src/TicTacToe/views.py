from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from . import models

def index_view(request: HttpRequest) -> HttpResponse:
    return render(request, "tictactoe/index.html")

def new_game(request: HttpRequest) -> HttpResponse:
    new_game_created = models.TTTGame()
    new_game_created.save()
    return render(request, "tictactoe/game.html", { "game": new_game_created })
