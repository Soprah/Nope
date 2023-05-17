import unittest

from src.gamelogic.deck.Deck import Deck
from src.gamelogic.player.Player import Player


class TestPlayerDrawCard(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()
        self.player = Player("Eric", 1)
        self.player.set_deck(self.deck)

    def test_player_empty_hand_before_start(self):
        self.assertEqual(len(self.player.hand), 0)

    def test_player_draws_card_for_hand(self):
        drawn_card = self.player.draw_card()
        card_on_hand = self.player.hand[0]
        self.assertEqual(drawn_card, card_on_hand)

    def test_player_draws_correct_card(self):
        top_card = self.deck.draw_stack[-1]
        drawn_card = self.player.draw_card()
        self.assertEqual(drawn_card, top_card)


if __name__ == '__main__':
    unittest.main()
