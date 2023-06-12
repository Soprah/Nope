import unittest

from src.dataconvert.DataConvert import DataConvert
from src.gamelogic.game.Game import Game
from src.gamelogic.player.Player import Player


class TestDataConvertToDictPreviousSelectedCards(unittest.TestCase):
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

    # Jeder Kartentyp (Number, Joker, Restart, View, SingleSel, MultipleSel)
    # Turn obj erstellen
    # Diese karten dem turn obj attribut zuweisen
    # expected_output definieren
    # zu testende methode ausführen und erg auf actual_output speichern
    # expected und actual vergleichen

    # GAME START
    def test_to_dict_previous_selected_cards_game_start(self):
        expected_output = []

        self.game.next_turn()
        actual_output = self.dc.to_dict_previous_selected_cards(self.game)

        self.assertEqual(actual_output, expected_output)

    # MID GAME - NORMAL
    def test_to_dict_previous_selected_cards_mid_game_normal_cards(self):
        expected_out_soft = [
            self.n_card.to_dict(),
            self.j_card.to_dict()
        ]
        expected_out_hard = [
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

        # Vorbereitungen
        first_turn = self.game.next_turn()
        first_turn.selected_cards = [self.n_card, self.j_card]
        second_turn = self.game.next_turn()

        # Funktion
        actual_output = self.dc.to_dict_previous_selected_cards(self.game)

        # Test
        self.assertEqual(expected_out_soft, actual_output)
        self.assertEqual(expected_out_hard, actual_output)

    # MID GAME - ACTION - VIEW
    def test_to_dict_previous_selected_cards_mid_game_view_card(self):
        expected_out_soft = [
            self.v_card.to_dict_actual_card(),
        ]
        expected_out_hard = [
            {
                "id": 92,
                "color_amount": 1,
                "color": ("blue",),
                "type": "action",
                "content": "view"
            },
        ]

        # Vorbereitungen
        first_turn = self.game.next_turn()
        first_turn.selected_cards = [self.v_card]
        second_turn = self.game.next_turn()

        # Funktion
        actual_output = self.dc.to_dict_previous_selected_cards(self.game)

        # Test
        self.assertEqual(expected_out_soft, actual_output)
        self.assertEqual(expected_out_hard, actual_output)

    # MID GAME - ACTION - SINGLE SEL
    def test_to_dict_previous_selected_cards_mid_game_single_sel_card(self):
        expected_out_soft = [
            self.ss_card.to_dict_actual_card(),
        ]
        expected_out_hard = [
            {
                "id": 97,
                "color_amount": 1,
                "color": ("green",),
                "type": "action",
                "content": "selection"
            },
        ]

        # Vorbereitungen
        first_turn = self.game.next_turn()
        first_turn.selected_cards = [self.ss_card]
        second_turn = self.game.next_turn()

        # Funktion
        actual_output = self.dc.to_dict_previous_selected_cards(self.game)

        # Test
        self.assertEqual(expected_out_soft, actual_output)
        self.assertEqual(expected_out_hard, actual_output)

    # MID GAME - ACTION - MULTIPLE SEL
    def test_to_dict_previous_selected_cards_mid_game_multiple_sel_card(self):
        expected_out_soft = [
            self.ms_card.to_dict_actual_card(),
        ]
        expected_out_hard = [
            {
                "id": 100,
                "color_amount": 4,
                "color": (("red"),("blue"), ("yellow"),("green")),
                "type": "action",
                "content": "selection"
            },
        ]

        # Vorbereitungen
        first_turn = self.game.next_turn()
        first_turn.selected_cards = [self.ms_card]
        second_turn = self.game.next_turn()

        # Funktion
        actual_output = self.dc.to_dict_previous_selected_cards(self.game)

        # Test
        self.assertEqual(expected_out_soft, actual_output)
        self.assertEqual(expected_out_hard, actual_output)

    # MID GAME - ACTION - RESTART
    def test_to_dict_previous_selected_cards_mid_game_restart_card(self):
        expected_out_soft = [
            self.r_card.to_dict_actual_card(),
        ]
        expected_out_hard = [
            {
                "id": 87,
                "color_amount": 4,
                "color": (("red"),("blue"), ("yellow"),("green")),
                "type": "action",
                "content": "restart"
            },
        ]

        # Vorbereitungen
        first_turn = self.game.next_turn()
        first_turn.selected_cards = [self.r_card]
        second_turn = self.game.next_turn()

        # Funktion
        actual_output = self.dc.to_dict_previous_selected_cards(self.game)

        # Test
        self.assertEqual(expected_out_soft, actual_output)
        self.assertEqual(expected_out_hard, actual_output)

if __name__ == '__main__':
    unittest.main()
