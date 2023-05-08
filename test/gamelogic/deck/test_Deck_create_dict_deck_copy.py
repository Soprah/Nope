import unittest

from src.gamelogic.deck.Deck import Deck


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_create_dict_copy_same_cards(self):
        deck_dict_copy = self.deck.create_dict_deck_copy(self.deck.cards)
        for card in self.deck.cards:
            self.assertEqual(deck_dict_copy.get(card.id), card)



if __name__ == '__main__':
    unittest.main()
