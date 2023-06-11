import unittest

from src.dataconvert.DataConvert import DataConvert
from src.gamelogic.card.Card import Card
from src.gamelogic.game.Game import Game
from src.gamelogic.player.Player import Player


class TestDataConvertToDictTopCard(unittest.TestCase):
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


# GAME START

    # NUMBER
    def test_to_dict_top_card_number(self):
        expected_out_soft = self.n_card.to_dict()
        expected_out_hard = {
                "id": 9,
                "color_amount": 1,
                "color": ("red",),
                "type": "number",
                "content": 2
            }

        # Vorbereitungen
        first_turn = self.game.next_turn()
        first_turn.top_card = self.n_card

        # Funktion
        actual_output = self.dc.to_dict_top_card(self.game)

        # Test
        self.assertEqual(expected_out_soft, actual_output)
        self.assertEqual(expected_out_hard, actual_output)

    # JOKER
    def test_to_dict_top_card_joker(self):
        expected_out_soft = self.j_card.to_dict()
        expected_out_hard = {
                "id": 101,
                "color_amount": 4,
                "color": (("red"),("blue"), ("yellow"),("green")),
                "type": "number",
                "content": 1
            }

        # Vorbereitungen
        first_turn = self.game.next_turn()
        first_turn.top_card = self.j_card

        # Funktion
        actual_output = self.dc.to_dict_top_card(self.game)

        # Test
        self.assertEqual(expected_out_soft, actual_output)
        self.assertEqual(expected_out_hard, actual_output)

    # RESTART
    def test_to_dict_top_card_restart(self):
        expected_out_soft = self.r_card.to_dict_top_card()
        expected_out_hard = {
                "id": 87,
                "color_amount": 4,
                "color": (("red"),("blue"), ("yellow"),("green")),
                "type": "number",
                "content": 1
            }

        # Vorbereitungen
        first_turn = self.game.next_turn()
        first_turn.top_card = self.r_card

        # Funktion
        actual_output = self.dc.to_dict_top_card(self.game)

        # Test
        self.assertEqual(expected_out_soft, actual_output)
        self.assertEqual(expected_out_hard, actual_output)

    # VIEW
    def test_to_dict_top_card_view(self):
        expected_out_soft = self.v_card.to_dict_top_card()
        expected_out_hard = {
                "id": -1,
                "color_amount": 1,
                "color": ("blue",),
                "type": "number",
                "content": 1
            }

        # Vorbereitungen
        first_turn = self.game.next_turn()
        first_turn.top_card = self.v_card

        # Funktion
        actual_output = self.dc.to_dict_top_card(self.game)

        # Test
        self.assertEqual(expected_out_soft, actual_output)
        self.assertEqual(expected_out_hard, actual_output)

    # SINGLE SEL
    def test_to_dict_top_card_single_selection(self):
        expected_out_soft = self.ss_card.to_dict_top_card()
        expected_out_hard = {
                "id": -1,
                "color_amount": 1,
                "color": ("green",),
                "type": "number",
                "content": 1
            }

        # Vorbereitungen
        first_turn = self.game.next_turn()
        first_turn.top_card = self.ss_card

        # Funktion
        actual_output = self.dc.to_dict_top_card(self.game)

        # Test
        self.assertEqual(expected_out_soft, actual_output)
        self.assertEqual(expected_out_hard, actual_output)

    # MULTIPLE SEL
    def test_to_dict_top_card_multiple_selection(self):
        expected_out_soft = self.ms_card.to_dict_top_card()
        expected_out_hard = {
                "id": -1,
                "color_amount": 4,
                "color": (("red"),("blue"), ("yellow"),("green")),
                "type": "number",
                "content": 1
            }

        # Vorbereitungen
        first_turn = self.game.next_turn()
        first_turn.top_card = self.ms_card

        # Funktion
        actual_output = self.dc.to_dict_top_card(self.game)

        # Test
        self.assertEqual(expected_out_soft, actual_output)
        self.assertEqual(expected_out_hard, actual_output)

# MID GAME

    # VIEW
    def test_to_dict_top_card_mid_game_viewcard(self):
        expected_out_hard = {
                "id": -1,
                "color_amount": 1,
                "color": ("red",),
                "type": "number",
                "content": 2
            }
        first_turn_dict = {
            "token": self.p1.id,
            "selected_cards": [self.v_card.id]
        }

        # Vorbereitungen

        # Erster Spielzug Simulation
        self.p1.hand = [self.v_card]
        self.game.deck.discard_stack[0] = self.n_card
        first_turn = self.game.next_turn()
        first_turn.top_card = self.n_card

        # Zweiter Spielzug Simulation
        second_turn = self.game.next_turn()
        self.game.switch_active_player()
        processed_dict = self.dc.net_to_gamelogic(first_turn_dict, self.game)
        processed_view_card = processed_dict.get("selected_cards")[0]
        second_turn.top_card = processed_view_card

        # Funktion
        actual_output = self.dc.to_dict_top_card(self.game)

        # Test
        self.assertEqual(expected_out_hard, actual_output)

    # SINGLE SEL

    # MULTIPLE SEL

if __name__ == '__main__':
    unittest.main()
