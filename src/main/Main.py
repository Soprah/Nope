from src.gamelogic.card.Card import Card
from src.gamelogic.card.JokerCard import JokerCard
from src.gamelogic.card.NumberCard import NumberCard
from src.gamelogic.card.RestartCard import RestartCard
from src.gamelogic.deck.Deck import Deck
from src.gamelogic.game.Game import Game
from src.gamelogic.player.Player import Player
from src.gamelogic.turn.Turn import Turn
from src.gamemanagement.GameManagement import GameManagement

"""
PLACEHOLDER
"""

# game = Game(Player("Eric", 3), Player("Marc", 19))
# game.run()
player = Player("Eric",3)
card = JokerCard(2, (("red"), ("blue"), ("yellow"), ("green")))
turn = Turn(player, card)
card1 = NumberCard(2, ("blue", "red"), 1)
card2 = RestartCard(9, (("red"), ("blue"), ("yellow"), ("green")))
card3 = NumberCard(2, ("green", "yellow"), 1)
player.hand = [card1, card2, card3]
expected_dict = {
    "red": [card1],
    "blue": [card1, card2],
    "yellow": [card2, card3],
    "green": [card3]
}
turn.possible_moves = turn.get_cards_matching_color()

print(len(expected_dict))
for key in expected_dict.keys():
    for card in expected_dict.get(key):
        print(f"Key: {key}, Karte: {card}")

print("**")

print(len(turn.possible_moves))
for key in turn.possible_moves.keys():
    for card in turn.possible_moves.get(key):
        print(f"Key: {key}, Karte: {card}")