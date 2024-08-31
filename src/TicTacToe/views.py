from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def index_view(request: HttpRequest):
    return render(request, "tictactoe/index.html")