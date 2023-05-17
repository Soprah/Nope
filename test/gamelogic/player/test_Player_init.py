import unittest

from src.gamelogic.deck.Deck import Deck
from src.gamelogic.player.Player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()
        self.player = Player(self.deck, "Eric")

    '''
    def test_player_unique_id(self):
        player2 = Player(self.deck, "Marc")
        self.assertNotEqual(self.player.id, player2.id)
    '''




if __name__ == '__main__':
    unittest.main()
