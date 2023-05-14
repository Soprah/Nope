from src.gamelogic.card.Card import Card
from src.gamelogic.deck.Deck import Deck
from src.gamelogic.game.Game import Game
from src.gamelogic.player.Player import Player
from src.gamelogic.turn.Turn import Turn

"""
PLACEHOLDER
"""

# game = Game("Eric", "Marc")
# game.turns.append(game.next_turn())
# print(game.active_player.name)
# game.switch_active_player()
# print(game.active_player.name)

game_list = {}
p1_id = 1
p2_id = 2
game_id = 10
game_id_2 = 20

game_list = {
    "p1_id": game_id,
    "p7_id": game_id_2
}

print(game_list.get("p1_id"))