import unittest

from src.dataconvert.DataConvert import DataConvert
from src.gamelogic.game.Game import Game
from src.gamelogic.player.Player import Player


class TestDataConvertToDictAmountOpponentHand(unittest.TestCase):
    def setUp(self):
        self.p1 = Player("Christina", 8)
        self.p2 = Player("Marc", 19)
        self.game = Game(self.p1, self.p2)
        self.dc = DataConvert()

        # color=red | number=2 | NUMBER
        self.n_card = self.game.deck.cards_dict.get(9)

        # color=red,blue,yellow,green | number=1 | JOKER
        self.j_card = self.game.deck.cards_dict.get(101)

        # color=red,blue,yellow,green | number=1 | RESTART
        self.r_card = self.game.deck.cards_dict.get(87)

        # color=blue | number=None | VIEW
        self.v_card = self.game.deck.cards_dict.get(92)

        # color=green | number=None | SINGLE SEL
        self.ss_card = self.game.deck.cards_dict.get(97)

        # color=red,blue,yellow,green | number=None | color=None | MULTIPLE SEL
        self.ms_card = self.game.deck.cards_dict.get(100)

    def tearDown(self):
        self.v_card.clear_theoretical_card()
        self.ss_card.clear_theoretical_card()
        self.ms_card.clear_theoretical_card()

    def test_to_dict_amount_opponent_hand(self):
        self.p1.hand = [self.n_card, self.j_card]
        self.p2.hand = [self.r_card]
        p1_first_turn_amount_expected = 1
        p2_first_turn_amount_expected = 2

        # Vorbereitung
        self.game.next_turn()

        # Test für Spieler 1
        p1_first_turn_amount_actual = self.dc.to_dict_amount_opponent_hand(self.game)
        self.assertEqual(p1_first_turn_amount_expected, p1_first_turn_amount_actual)

        # Vorbereitung
        self.game.next_turn()

        # Test für Spieler 2
        p2_first_turn_amount_actual = self.dc.to_dict_amount_opponent_hand(self.game)
        self.assertEqual(p2_first_turn_amount_expected, p2_first_turn_amount_actual)



if __name__ == '__main__':
    unittest.main()
