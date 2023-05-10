import unittest

from src.gamelogic.deck.Deck import Deck
from src.gamelogic.player.Player import Player


class TestPlayerDrawAndDiscardCard(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
        self.player = Player(self.deck, "Eric")

    def test_draw_and_discard_card(self):
        drawn_card = self.player.draw_card()
        discarded_card = self.player.discard_card(drawn_card)
        self.assertEqual(drawn_card, discarded_card)
        self.assertEqual(self.deck.discard_stack[0], discarded_card)



if __name__ == '__main__':
    unittest.main()
