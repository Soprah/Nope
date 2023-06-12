import unittest

from src.gamelogic.deck.Deck import Deck
from src.gamelogic.game.Game import Game
from src.gamelogic.player.Player import Player


class TestDeckClearTheoreticalReferences(unittest.TestCase):
    def setUp(self):
        # Spielvorbereitung
        self.p1 = Player("Christina", 8)
        self.p2 = Player("Marc", 19)
        self.game = Game(self.p1, self.p2)

        # Karten
        self.g_1 = self.game.deck.cards_dict.get(5)
        self.y_1 = self.game.deck.cards_dict.get(7)
        self.view_red = self.game.deck.cards_dict.get(91)
        self.selection_blue = self.game.deck.cards_dict.get(96)
        self.multi_sel = self.game.deck.cards_dict.get(100)

    def test_clear_theoretical_references(self):
        to_clear_list = [
            self.g_1,
            self.y_1,
            self.view_red,
            self.selection_blue,
            self.multi_sel
        ]

        # Vorbereitung
        self.view_red.set_theoretical_card(self.y_1)
        self.assertEqual(("yellow",), self.view_red.get_color())
        self.assertEqual(1 , self.view_red.get_number())

        self.selection_blue.set_theoretical_card(2)
        self.assertEqual(2, self.selection_blue.get_number())

        self.multi_sel.set_theoretical_card(3, ("blue",))
        self.assertEqual(3, self.multi_sel.get_number())
        self.assertEqual(("blue",), self.multi_sel.get_color())

        # Funktion
        cleared_list = self.game.deck.clear_theoretical_references(to_clear_list)

        # Richtige Anzahl
        self.assertEqual(5, len(cleared_list))

        # Gleiche Elemente enthalten
        for card in cleared_list:
            self.assertIn(card, to_clear_list)

        # Referenz erfolgreich zurückgesetzt
        self.assertEqual(("red",), self.view_red.get_color())
        self.assertEqual(1, self.view_red.get_number())

        self.assertEqual(1, self.selection_blue.get_number())

        self.assertEqual(1, self.multi_sel.get_number())
        self.assertEqual((("red"), ("blue"), ("yellow"), ("green")), self.multi_sel.get_color())


if __name__ == '__main__':
    unittest.main()
