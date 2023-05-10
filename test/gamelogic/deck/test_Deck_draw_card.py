import unittest

from src.gamelogic.deck.Deck import Deck


class TestDeckDrawCard(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_draw_card_removes_card(self):
        length_draw_stack = len(self.deck.draw_stack)
        top_card = self.deck.draw_stack[-2]
        self.deck.draw_card()
        # Länge des Nachziehstapels verringert sich um 1
        self.assertEqual(len(self.deck.draw_stack), length_draw_stack - 1)
        # Oberste Karte wird zurückgegeben
        self.assertEqual(self.deck.draw_card(), top_card)


if __name__ == '__main__':
    unittest.main()
