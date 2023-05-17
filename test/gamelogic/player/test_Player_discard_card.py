import unittest

from src.gamelogic.deck.Deck import Deck
from src.gamelogic.player.Player import Player


class TestPlayerDiscardCard(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()
        self.player = Player("Eric", 1)
        self.player.set_deck(self.deck)

    def test_player_discard_card_exists(self):
        with self.assertRaises(ValueError):
            self.player.discard_card(self.player.deck.cards[0])

    def test_player_discard_card_off_hand(self):
        self.player.draw_card()
        hand_card = self.player.hand[0]
        discarded_card = self.player.discard_card(self.player.hand[0])
        self.assertEqual(discarded_card, hand_card)



if __name__ == '__main__':
    unittest.main()
