import unittest

from src.gamelogic.deck.Deck import Deck
from src.gamelogic.player.Player import Player


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()
        self.player = Player(self.deck, "Eric")


if __name__ == '__main__':
    unittest.main()
