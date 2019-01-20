from django.shortcuts import render
import random
import parse

# Create your views here.

from .models import Game
from .models import Card
from .models import Player

def index(request):
    template_name = 'pokergame/index.html'
    if not Game.objects.exists():
        game = Game()
        createdeck(game)
        game.players.create(card = game.deck.objects.all().first())
        game.save()
    else:
        game = Game.objects.all().first()
        game.players.create(game.deck.objects.all().first())
    context = {'players': game.players}
    return render(request, template_name, context)

def createdeck(game):
    temp = []
    for suit in ['S', 'C', 'H', 'D']:
        for val in range(13):
            temp.append('{}{:d}'.format(suit, val))
    random.shuffle(temp)
    for str in temp:
        parser = parse.compile('{}{}')
        parsed = parser.parse(str)
        game.deck.create(suit = parsed[0], val = int(parsed[1]))