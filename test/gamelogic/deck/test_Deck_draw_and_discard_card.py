import unittest

from src.gamelogic.deck.Deck import Deck


class TestDeckDrawAndDiscard(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_draw_and_discard_card_same_card(self):
        card = self.deck.draw_card()
        self.assertEqual(self.deck.discard_card(card), self.deck.discard_stack[0])

    def test_empty_deck_draw_card(self):
        # Initialisiert den Ablagestapel, sodass es eine Karte hat
        old_top_card = self.deck.draw_card()
        self.deck.discard_card(old_top_card)
        # Geben dem Spieler eine Karte, die wir nachher zum Vergleich nutzen
        new_top_card = self.deck.draw_card()
        self.deck.discard_card(new_top_card)
        new_top_card = self.deck.draw_card()
        self.deck.discard_card(new_top_card)
        self.assertEqual(3, len(self.deck.discard_stack))
        # Machen den nachziehstapel leer
        while len(self.deck.draw_stack) > 0:
            self.deck.draw_card()
        self.deck.draw_card()
        self.assertEqual(1, len(self.deck.draw_stack))
        self.assertEqual(1, (len(self.deck.discard_stack)))
        self.assertEqual(new_top_card, self.deck.discard_stack[0])



if __name__ == '__main__':
    unittest.main()
