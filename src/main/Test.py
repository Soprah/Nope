from src.gamelogic.card.NumberCard import NumberCard
from src.gamelogic.card.SelectionCard import SelectionCard
from src.gamelogic.card.ViewCard import ViewCard
from src.gamelogic.game.Game import Game
from src.gamelogic.player.Player import Player
from src.dataconvert.DataConvert import DataConvert
from src.gamelogic.turn.Turn import Turn
from src.gamemanagement.GameManagement import GameManagement

p1 = Player("Eric", "33")
p2 = Player("Marc", "19")
game = Game(p1, p2)
# for c in game.deck.cards:
#     print(c)

dictionary = {
    "own_hand_cards": [
        {"id": 1},
        {"id": 2},
        {"id": 3}
    ]
}

def get_card_ids(dictionary):
    card_ids = []
    own_hand_cards = dictionary.get("own_hand_cards", [])
    for card_dict in own_hand_cards:
        card_id = card_dict.get("id")
        if card_id is not None:
            card_ids.append(card_id)
    return card_ids


card_ids = get_card_ids(dictionary)
print(card_ids)

