from src.gamelogic.card.Card import Card
from src.gamelogic.deck.Deck import Deck
from src.gamelogic.game.Game import Game
from src.gamelogic.player.Player import Player
from src.gamelogic.turn.Turn import Turn
from src.gamemanagement.GameManagement import GameManagement

"""
PLACEHOLDER
"""

gm = GameManagement()
gm.assign_player_to_game(1, "Eric", 2, "Marc")
gm.assign_player_to_game(3, "Eric", 4, "Marc")
game = gm.get_game(1)
print(game.active_player)
print(game.player_1)
print(game.player_2)