from django.http import JsonResponse
from .models import Player

def get_players(request):
    players = Player.objects.all()
    print(players)
    player_list = [{'name': player.name, 'position': player.position} for player in players]
    response_data = {'players': player_list}
    return JsonResponse(response_data)
