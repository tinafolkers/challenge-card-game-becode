"""
create a class `Player` that contains these attributes:

- `cards/hands` which is a list of `Card`. *(you will need to import `Card` from `card.py`)*.
- `turn_count` which is an int starting a 0.
- `number_of_cards` which is an int starting at 0.
- `history` which is a list of `Card` that will contain all the cards played by the player.
  """

import random
from card import Card

class Player():
    def __init__(self, player_name, hands, turn_count, number_of_cards, history):
        self.player_name = player_name
        self.hands = hands
        self.turn_count = turn_count
        self.number_of_cards = number_of_cards
        self.history = history #Empty List of played cards to Append
    
    """And some methods:

- `play()` that will:
  - **randomly** pick a `Card` in `cards`.
  - Add the `Card` to the `Player`'s `history`.
  - Print: `{PLAYER_NAME} {TURN_COUNT} played: {CARD_NUMBER} {CARD_SYMBOL_ICON}`.
  - return the `Card`.
  """
    
    def play(self): 
        RandomNumber = random.randint(0,len(self.hands)-1) #Generates Random Card
        random_card = self.hands[RandomNumber]
        self.history.append(random_card)
        
        print ("{self.player_name} {self.turn_count} played: {random_card.color} {random_card.value} {random_card.icon}")
        return random_card

"""Create a `Deck` class that contains:

- An attribute `cards` which is gonna contain a list of instances of `Card`.
- A `fill_deck()` method that will fill `card()` with a complete card game *(an instance of  'A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K' for each possible symbol [♥, ♦, ♣, ♠])*. Your deck should contain **52 cards at the end**.
- A `shuffle()` method that will shuffle all the `Card` instances of `cards`.
- A `distribute()` that will take a list of `Player` as parameter and will distribute the cards evenly between all the players."""
    
class Deck():
    def __init__(self,cards = []):
        self.cards = cards
    
    def fill_deck(self):
        icon = ['♥', '♦', '♣', '♠']
        value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        for i in icon:
            for v in value:
                self.cards.append(Card(v, i))

    def shuffle(self):     
        random.shuffle(self.cards)
        return self.cards
            
            
    def distribute(self, list_of_players: list):
        nr_of_cards = len(self.cards) // len(list_of_players)
        for p in list_of_players:
            for i in range(0, nr_of_cards):
                p.hands.append(self.cards[0]) 
                self.cards.pop(0)
                i+=1      
        return list_of_players
            
            
            
            
