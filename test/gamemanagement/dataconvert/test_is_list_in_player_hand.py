import unittest

from src.gamelogic.card.NumberCard import NumberCard
from src.gamelogic.card.SelectionCard import SelectionCard
from src.gamelogic.game.Game import Game
from src.gamelogic.player.Player import Player
from src.gamemanagement.DataConvert import DataConvert


class TestDataConvertIsListInPlayerHand(unittest.TestCase):
    def setUp(self):
        self.dc = DataConvert()
        self.p1 = Player("Eric", 33)
        self.p2 = Player("Marc", 99)
        self.game = Game(self.p1, self.p2)

    # IDs sind vorhanden
    def test_is_list_in_player_hand_true(self):
        # NumberCard, id=11, color=("blue",), number=2
        card_1 = self.game.deck.cards_dict.get(11)
        self.p1.hand = [card_1]
        id_list = [card_1.id]

        self.assertTrue(self.dc.is_list_in_player_hand(id_list, self.game))

    # IDs sind nicht vorhanden
    def test_is_list_in_player_hand_false(self):
        id_list = [123, 321]
        self.assertFalse(self.dc.is_list_in_player_hand(id_list, self.game))

if __name__ == '__main__':
    unittest.main()