import unittest

from src.gamelogic.deck.Deck import Deck
from src.gamelogic.game.Game import Game
from src.gamelogic.player.Player import Player


class TestDeckDrawAndDiscard(unittest.TestCase):

    def setUp(self):
        # self.deck = Deck()

        # # Spielvorbereitung
        self.p1 = Player("Christina", 8)
        self.p2 = Player("Marc", 19)
        self.game = Game(self.p1, self.p2)

        # Karten zum Prüfen
        self.y_1 = self.game.deck.cards_dict.get(7)
        self.view_red = self.game.deck.cards_dict.get(91)
        self.selection_blue = self.game.deck.cards_dict.get(96)
        self.multi_sel = self.game.deck.cards_dict.get(100)

    def test_draw_and_discard_card_same_card(self):
        drawn_card = self.game.active_player.draw_card()
        discarded_card = self.game.active_player.discard_card(drawn_card)
        self.assertEqual(drawn_card, discarded_card)

    def test_empty_deck_draw_card(self):
        # Vorbereitung

        # Spielerhand leeren
        self.p1.hand.clear()
        self.p2.hand.clear()

        # Testkarten
        test_cards = [
            self.y_1,
            self.view_red,
            self.selection_blue,
            self.multi_sel
        ]

        # Alle Karten des Nachziehstapels in den Ablagestapel kopieren

        self.game.deck.discard_stack = self.game.deck.draw_stack.copy()
        # ablagestapel.append(self.y_1)
        # self.assertIsNot(ablagestapel, nachziehstapel)
        self.assertEqual(len(self.game.deck.draw_stack), 87)  # Spieler besitzen auch Karten in Hand

        # Nachziehstapel leeren
        self.game.deck.draw_stack.clear()
        self.assertTrue(len(self.game.deck.draw_stack) == 0)

        # Oberste Karte des Ablagestapels zwischenspeichern zum Prüfen nachher
        top_card = self.game.deck.discard_stack[-1]

        # Action Card Referenzen setzen
        self.view_red.set_theoretical_card(self.y_1)
        self.assertEqual(("yellow",), self.view_red.get_color())
        self.assertEqual(1, self.view_red.get_number())

        self.selection_blue.set_theoretical_card(2)
        self.assertEqual(2, self.selection_blue.get_number())

        self.multi_sel.set_theoretical_card(3, ("blue",))
        self.assertEqual(3, self.multi_sel.get_number())
        self.assertEqual(("blue",), self.multi_sel.get_color())

        # Sichergehen, dass Testkarten im Ablagestapel sind
        for card in test_cards:
            if card not in self.game.deck.discard_stack:
                self.game.deck.discard_stack.append(card)
                self.assertIn(card, self.game.deck.discard_stack)


        # Funktion
        self.p1.draw_card()

        # Tests

        # Nachziehstapel
        # Besitzt Karten
        self.assertTrue(len(self.game.deck.draw_stack) > 0)
        self.assertTrue(len(self.game.deck.draw_stack) == 88)

        # Ablagestapel
        # Besitzt nur eine Karte
        self.assertTrue(len(self.game.deck.discard_stack) == 1)
        # Top Card behält Referenz
        self.assertIsNotNone(self.game.deck.discard_stack[-1].theoretical_card)

        # Referenzen der gemischten Karten wurden gelöscht
        self.assertIsNone(self.view_red.theoretical_card)
        self.assertIsNone(self.selection_blue.theoretical_card)

        # Spieler besitzt eine Karte mehr
        self.assertTrue(len(self.game.active_player.hand) == 1)



if __name__ == '__main__':
    unittest.main()
