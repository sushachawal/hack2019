import random
import math
import time

class Card:
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

class Player:
	def __init__(self,id,isAI):
		self.id = id
		self.isAI = isAI
		self.chips = 20
		self.bet = 1
		self.card = None
		self.hasFolded = False
	def confirmBet(self):
		time.sleep(1)
		return 5
		
class HumanPlayer(Player):
	def confirmBet(self):
		
		valid_input = False
		while valid_input == False:
			user_input = raw_input("What are you betting(Note: 0 for call, 'fold' will fold) ?: ")
			try:
				val = int(user_input)
				val = math.floor(val)
				if val < 0 :
					val = 0
				print("You entered " + str(user_input))
				valid_input = True
			except ValueError:
				if user_input == 'fold' : 
					val = -1
					valid_input = True
				else :
					print("Incorrect Input, try again...")				
		return val


class Game:
	def __init__(self):		
		self.cardDeck = []
		self.players = []
		
		
		for suit in ['S','C','H','D']:
			for value in range(13):
				self.cardDeck.append(Card(suit,value))
					
		random.shuffle(self.cardDeck)
		
		self.players.append(Player('ai1',0))
		#self.players.append(Player('ai2',0, self.cardDeck[1]))
		self.players.append(HumanPlayer('human',0))
			
	def main(self):
		startingPlayerIndex = 0
		while len(self.cardDeck) > len(self.players) and len(self.players) > 1	:	
			currentPlayerIndex = startingPlayerIndex
			activeBetters = [1] * len(self.players)
			
			maxBet = 1;
			maxBetPlayer = startingPlayerIndex;
			firstMove = True
			
			# GIVE PLAYERS CARDS & SET INITIAL BET
			for player in self.players :
				player.card = self.cardDeck.pop(0)
				
			
			while(currentPlayerIndex != maxBetPlayer or firstMove == True)	:
				firstMove = False
				print('*' * 10)
				print('PLAYER TURN: ' + 'Player ' + str(self.players[currentPlayerIndex].id)) 
				print('Current Bets:')
				for player in self.players : 
					plInfo = '- ' + 'Player ' + str(player.id) + '(+' + str(player.card.value) +'+)'+ '(' + str(player.chips) +')'+ ' - ' + str(player.bet)
					if player.hasFolded == True : 
						plInfo = plInfo + '(folded)'
					print(plInfo)
				
				bet = self.players[currentPlayerIndex].confirmBet()
				
				if bet == -1 :# FOLD
					self.players[currentPlayerIndex].hasFolded = True
					
				elif bet == 0 : # CALL
					if self.players[currentPlayerIndex].chips < maxBet :
						self.players[currentPlayerIndex].bet = self.players[currentPlayerIndex].chips
					else : 
						self.players[currentPlayerIndex].bet = maxBet
				else : # RAISE
					if self.players[currentPlayerIndex].chips < (maxBet + int(bet)): 
						self.players[currentPlayerIndex].bet = self.players[currentPlayerIndex].chips
					else : 
						maxBet = maxBet + int(bet)
						self.players[currentPlayerIndex].bet = maxBet
						maxBetPlayer = currentPlayerIndex
			
				
				validNextPlayerTurn = False
				while(validNextPlayerTurn == False) :
					currentPlayerIndex = (currentPlayerIndex + 1) % len(self.players)
					if self.players[currentPlayerIndex].hasFolded == False :
						validNextPlayerTurn = True
					if self.players[currentPlayerIndex].bet == self.players[currentPlayerIndex].chips : 
						validNextPlayerTurn = False
			currentWinner = []
			maxVal = -1
			pot = 0
			for player in self.players :
				player.chips -= player.bet
				pot += player.bet
				player.bet = 1
				if player.hasFolded != True :
					if player.card.value > maxVal :
						currentWinner = []
						currentWinner.append(player)
						maxVal = player.card.value
					elif player.card.value == maxVal :
						currentWinnder.append(player)
				else : 
					player.hasFolded = False
				
			for winner in currentWinner : 
				winner.chips += pot / len(currentWinner)
			# REMOVE PLAYERS IF NECESSARY
			startingPlayerIndex = (startingPlayerIndex + 1) % len(self.players)	
			
			
		
	

game = Game()
game.main()
