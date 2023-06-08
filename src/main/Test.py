from src.gamelogic.card.NumberCard import NumberCard
from src.gamelogic.card.ViewCard import ViewCard
from src.gamelogic.game.Game import Game
from src.gamelogic.player.Player import Player
from src.gamemanagement.DataConvert import DataConvert

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

dc = DataConvert()
card = game.deck.cards_dict.get(97)
p1.hand = [card]
client_dict = {
    "token": 33,
    "selected_cards": [card.id],
    "chosen_number": 2,
    "chosen_color": ("blue",)
}

id_list = client_dict.get("selected_cards")
if dc.is_list_in_player_hand(id_list, game):
    cards = dc.build_card_objects(id_list, game)
client_dict["selected_cards"] = cards

# checked_dict = dc.execute_steps_for_selection_card(client_dict, game)
# edited_card = checked_dict.get("selected_cards")[0]
raw_card = client_dict.get("selected_cards")[0]
print(raw_card)
edited_card = raw_card
raw_card.set_theoretical_card(client_dict.get("chosen_number"), client_dict.get("chosen_color"))
print(edited_card)