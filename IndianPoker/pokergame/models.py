from django.db import models

# Create your models here.

MAX_PLAYERS = 2

class Card(models.Model):
    suit = models.CharField(max_length=1, default='S')
    value = models.IntegerField(default=2)


class Player(models.Model):
    available_chips = models.IntegerField(default=20)
    AI = models.BooleanField(default=False)
    current_bet = models.IntegerField(default=0)
    card = models.OneToOneField(Card, on_delete=models.CASCADE)
    winner = models.BooleanField(default=False)
    turn = models.BooleanField(default=False)


class Game(models.Model):
    turn = models.IntegerField(default=0, primary_key=True)
    players = models.ForeignKey(Player, on_delete=models.CASCADE)
    deck = models.ForeignKey(Card, on_delete=models.CASCADE)



