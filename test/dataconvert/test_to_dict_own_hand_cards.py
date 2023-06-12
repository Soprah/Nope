import unittest

from src.dataconvert.DataConvert import DataConvert
from src.gamelogic.game.Game import Game
from src.gamelogic.player.Player import Player


class MyTestCase(unittest.TestCase):
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

    def test_to_dict_own_hand_cards(self):
        self.p1.hand = [self.n_card, self.j_card]
        self.p2.hand = [self.r_card]

        p1_expected_out_soft = [
            self.n_card.to_dict(),
            self.j_card.to_dict()
        ]
        p1_expected_out_hard = [
            {
                "id": 9,
                "color_amount": 1,
                "color": ("red",),
                "type": "number",
                "content": 2
            },
            {
                "id": 101,
                "color_amount": 4,
                "color": (("red"),("blue"), ("yellow"),("green")),
                "type": "number",
                "content": 1
            }
        ]

        p2_expected_out_soft = [
            self.r_card.to_dict_actual_card()
        ]
        p2_expected_out_hard = [
            {
                "id": 87,
                "color_amount": 4,
                "color": (("red"),("blue"), ("yellow"),("green")),
                "type": "action",
                "content": "restart"
            },
        ]

        # Vorbereitungen für P1
        first_turn = self.game.next_turn()

        # Funktion P1
        actual_output = self.dc.to_dict_own_hand_cards(self.game)

        # Test P1
        self.assertEqual(p1_expected_out_soft, actual_output)
        self.assertEqual(p1_expected_out_hard, actual_output)

        # Vorbereitungen für P2
        first_turn = self.game.next_turn()

        # Funktion P2
        actual_output = self.dc.to_dict_own_hand_cards(self.game)

        # Test P2
        self.assertEqual(p2_expected_out_soft, actual_output)
        self.assertEqual(p2_expected_out_hard, actual_output)

if __name__ == '__main__':
    unittest.main()
