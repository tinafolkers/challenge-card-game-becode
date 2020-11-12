import sys, os
sys.path.extend([f'./{name}' for name in os.listdir(".") if os.path.isdir(name)])

from utils.card import Symbol
from utils.card import Card

from utils.player import Player
from utils.player import Deck

from utils.game import Board

main_board = Board()
main_board.start_game()



