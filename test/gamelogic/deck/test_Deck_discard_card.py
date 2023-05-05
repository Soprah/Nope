import unittest

from src.gamelogic.card.Card import Card
from src.gamelogic.card.NumberCard import NumberCard
from src.gamelogic.deck.Deck import Deck


class TestDeckDiscardCard(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_discard_card_type(self):
        card = self.deck.draw_stack.pop()
        self.deck.discard_card(card)
        self.assertIsInstance(self.deck.discard_stack[0], Card)

    def test_discard_card_exists(self):
        # Gültige Karte, aber gibt es nicht im Deck
        card = NumberCard(47, ("red"), 3)
        with self.assertRaises(ValueError):
            self.deck.discard_card(card)

    def test_discarded_card_on_discard_stack(self):
        card = self.deck.draw_card()
        self.assertEqual(self.deck.discard_card(card), self.deck.discard_stack[0])

if __name__ == '__main__':
    unittest.main()
