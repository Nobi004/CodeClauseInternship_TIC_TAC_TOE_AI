# CodeClauseInternship_Tic-Tac-Toe-AI/urls.py

from django.contrib import admin
from django.urls import path, include  # Make sure to import include
from . import views

urlpatterns = [
    path('', views.game_view, name='game_view'),  # Correct usage
    path('play_move/', views.play_move, name='play_move'),
    path('Quit/', views.quit_game, name='quit_game'),    # New quit URL
    path("api/", views.api_view),
]
