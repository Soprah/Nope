import unittest

from src.gamelogic.card.ViewCard import ViewCard


class TestViewCardToDictTopCard(unittest.TestCase):
    def setUp(self):
        self.view_card = ViewCard(1, ("blue"))

    # Erste Karte im Ablagestapel: ViewCard
    def test_to_dict_top_card_start_game(self):
        expected_dict = {
            "id": -1,
            "color_amount": 1,
            "color": ("blue",),
            "type": "number",
            "content": 1
        }
        actual_dict = self.view_card.to_dict_top_card()
        self.assertDictEqual(expected_dict, actual_dict)

    # Erste Karte im Ablagestapel: NumberCard
    # Zweite Karte im Ablagestapel: ViewCard

    # Erste Karte im Ablagestapel: JokerCard
    # Zweite Karte im Ablagestapel: ViewCard

    # Erste Karte im Ablagestapel: RestartCard
    # Zweite Karte im Ablagestapel: ViewCard

    # Erste Karte im Ablagestapel: SelectionCard
    # Zweite Karte im Ablagestapel: ViewCard

    # Erste Karte im Ablagestapel:



if __name__ == '__main__':
    unittest.main()
