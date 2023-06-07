from src.gamelogic.card.NumberCard import NumberCard
from src.gamelogic.card.ViewCard import ViewCard
from src.gamelogic.game.Game import Game
from src.gamelogic.player.Player import Player

# game = Game(Player("Eric", 3), Player("Marc", 19))
# print("Karte vorher", game.deck.discard_stack[-1])
# # game.deck.discard_stack[-1] = ViewCard(1, ("blue"))
# new_turn = game.next_turn()
# print(len(game.deck.discard_stack))
# game_sent_turn_data = game.send_turn_data(new_turn)
# for key in game_sent_turn_data.keys():
#     print(f"Schlüssel: {key}, Wert: {game_sent_turn_data.get(key)}")

'''
turn_data = {
    "previous_selected_cards": [],
    "top_card": {
        "id": "-1",
        "color_amount": "1",
        "colors": ["yellow"],
        "type": "number",
        "content": "1"
    },
    "amount_opponent_cards": 5,
    "own_hand_cards": ["card1", "card2", "card3"]
}

print(turn_data.get("top_card").get("color_amount"))

import json

class Card:
    def __init__(self, card_id, color):
        self.card_id = card_id
        self.color = color

    def to_dict(self):
        return {
            "card_id": self.card_id,
            "color": self.color
        }

cards = [
    Card("1", "red"),
    Card("2", "blue"),
    Card("3", "green")
]

# Serialisierung der Liste von Kartenobjekten
cards_data = [card.to_dict() for card in cards]
json_data = json.dumps(cards_data)
'''

# first_top_card = ViewCard(4, ("blue"))
# second_top_card = ViewCard(2, ("green"))
# second_top_card.set_theoretical_card(first_top_card)
# third_top_card = ViewCard(2, ("red"))
# third_top_card.set_theoretical_card(second_top_card)
# expected_dict = {
#     "id": -1,
#     "color_amount": 1,
#     "color": ("blue",),
#     "type": "number",
#     "content": 1
# }
# actual_dict = third_top_card.to_dict_top_card()
# print(actual_dict)