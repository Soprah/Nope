import unittest

from src.gamelogic.deck.Deck import Deck
class TestDeck(unittest.TestCase):


    def test_singleton_instance(self):
        deck1 = Deck()
        deck2 = Deck()
        self.assertIs(deck1, deck2)



if __name__ == '__main__':
    unittest.main()
