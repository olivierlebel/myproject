from django.urls import path
from . import views

urlpatterns = [
    path('players/', views.get_players, name='get_players'),
]
