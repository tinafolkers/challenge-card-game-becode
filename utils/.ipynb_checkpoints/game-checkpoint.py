"""
In `game.py` create:

A class called `Board` that contains:

- An attribute `players` that is a list of `Player`. It will contain all the players that are playing.
- An attribute `turn_count` that is an int.
- An attribute `active_cards` that will contain the last card played by each player.
- An attribute `history_cards` that will contains all the cards played except the `active_cards`.

- A method `start_game()` that will:
  - Starts the game,
  - Fill a `Deck`,
  - Distribute the cards of the `Deck` to the players.
  - Make each `Player` `play()` a `Card` , where each player should only play 1 card per turn, and all players have to play at each turn until they have no card left.
  - At the end of each turn, print:
    - The turn count.
    - The list of active cards.
    - The number of cards in the `history_cards`.
"""
from card import Card
from player import Player, Deck

class Board ():
    def __init__(self, list_of_players: list=[], turn_count: int=0, active_cards: list=[], history_cards: list=[]):
        self.list_of_players = list_of_players
        self.turn_count = turn_count
        self.active_cards = active_cards
        self.history_cards = history_cards
    
    def start_game(self):
        
        string_list = input ("Enter the names of players separated by commas: ")
        list_of_players = string_list.split(',')
        players = []
        for i in list_of_players:
            players.append(Player(i, [], 0, 0, []))
        deck = Deck()
        deck.fill_deck()
        deck.shuffle()
        list_players = deck.distribute(players)
        turn_count = 0                    
        for n in range (0, len(list_players[0].hands)):
            turn_count += 1
            print("turn : " + str(turn_count))
            for p in list_players:
                c = p.hands[0]
                self.active_cards.append(p.hands[0])
                p.hands.remove(c)          
                print ("{} played: ".format(p.player_name) + c.value,c.icon)
            #print (self.history_cards, self.history_cards)
            self.history_cards.extend (self.active_cards)
                            
            
                             
                
                
                             
                                 
                                         
                             
                             
       
       
      