import unittest

from src.gamelogic.card.NumberCard import NumberCard
from src.gamelogic.deck.Deck import Deck
class TestDeck(unittest.TestCase):


    def test_singleton_instance(self):
        deck1 = Deck()
        deck2 = Deck()
        self.assertIs(deck1, deck2)

    def test_deck_contains_20_one_color_cards(self):
        count = 0
        deck = Deck()
        cards = deck.cards
        for card in cards:
            if card.color_amount == 1 and isinstance(card, NumberCard):
                count += 1
        self.assertEqual(count, 20)

    def test_deck_contains_correct_20_one_color_cards(self):
        id_count = 1
        n = [1, 2, 3]
        f = [("red"), ("blue"), ("green"), ("yellow")]
        k = []

        # Einfarbige Karten: 20 Stück
        for number in n:
            for farbe in f:
                if number == 3:
                    k.append(NumberCard(1, farbe, id_count, number))
                    id_count = id_count + 1
                else:
                    for i in range(2):
                        k.append(NumberCard(1, farbe, id_count, number))
                        id_count = id_count + 1

        # Test the length of the deck
        assert len(k) == 20

        # Test the number of cards with number 1, 2, and 3
        assert sum(card.number == 1 and card.color_amount == 1 for card in k) == 8
        assert sum(card.number == 2 and card.color_amount == 1 for card in k) == 8
        assert sum(card.number == 3 and card.color_amount == 1 for card in k) == 4

    def test_deck_contains_correct_66_two_color_cards(self):
        id_count = 1
        f = [("red", "blue"), ("red", "green"), ("red", "yellow"), ("blue", "green"), ("blue", "yellow"),
             ("green", "yellow")]
        k = []

        for i in range(2):
            for farbe in f:
                # 24Karten für Zahl 1
                k.append(NumberCard(2, (farbe[0], farbe[1]), id_count, 1))
                id_count = id_count + 1
                k.append(NumberCard(2, (farbe[1], farbe[0]), id_count, 1))
                id_count = id_count + 1
                # 24Karten für Zahl 2
                k.append(NumberCard(2, (farbe[0], farbe[1]), id_count, 2))
                id_count = id_count + 1
                k.append(NumberCard(2, (farbe[1], farbe[0]), id_count, 2))
                id_count = id_count + 1
        for farbe in f:
            # 18 Karten für Zahl 3
            k.append(NumberCard(2, (farbe[0], farbe[1]), id_count, 3))
            id_count = id_count + 1
            k.append(NumberCard(2, (farbe[1], farbe[0]), id_count, 3))
            id_count = id_count + 1
            k.append(NumberCard(2, (farbe[0], farbe[1]), id_count, 3))
            id_count = id_count + 1

        # Test the length of the deck
        assert len(k) == 66

        # Test the number of cards with number 1, 2, and 3
        assert sum(card.number == 1 and card.color_amount == 2 for card in k) == 24
        assert sum(card.number == 2 and card.color_amount == 2 for card in k) == 24
        assert sum(card.number == 3 and card.color_amount == 2 for card in k) == 18

if __name__ == '__main__':
    unittest.main()
