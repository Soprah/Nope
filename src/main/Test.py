from src.gamelogic.card.NumberCard import NumberCard
from src.gamelogic.card.ViewCard import ViewCard
from src.gamelogic.game.Game import Game
from src.gamelogic.player.Player import Player
from src.gamemanagement.DataConvert import DataConvert
from src.gamemanagement.GameManagement import GameManagement

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
p1 = Player("Eric", 33)
p2 = Player("Marc", 19)
game = Game(p1, p2)
# for c in game.deck.cards:
#     print(c)
hand = [
    game.active_player.hand[0].id,
    game.active_player.hand[0].id,
    game.active_player.hand[2].id,
]
print(hand)