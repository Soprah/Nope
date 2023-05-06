import unittest

from src.gamelogic.deck.Deck import Deck
from src.gamelogic.player.Player import Player
from src.gamelogic.turn.Turn import Turn


class TestTurnInit(unittest.TestCase):


    def setUp(self):
        self.deck = Deck()
        self.player = Player(self.deck, "eric")
        self.first_top_card = self.deck.initialize_discard_stack()

    def test_Turn_init_attributes_initialised(self):
        turn = Turn(self.player, self.first_top_card)
        self.assertEqual(turn.top_card, self.first_top_card)
        self.assertEqual(turn.player, self.player)
        self.assertEqual(len(turn.selected_cards), 0)
        self.assertEqual(len(turn.possible_moves), 0)

    def test_Turn_init_player_type(self):
        with self.assertRaises(TypeError):
            turn = Turn(2, self.first_top_card)

    def test_Turn_init_card_type(self):
        with self.assertRaises(TypeError):
            turn = Turn(self.player, 2)

if __name__ == '__main__':
    unittest.main()
