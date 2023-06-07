import unittest

from src.gamelogic.card.JokerCard import JokerCard
from src.gamelogic.card.NumberCard import NumberCard
from src.gamelogic.card.RestartCard import RestartCard
from src.gamelogic.card.SelectionCard import SelectionCard
from src.gamelogic.card.ViewCard import ViewCard


class TestViewCardToDictTopCard(unittest.TestCase):

    # Erste Karte im Ablagestapel: ViewCard
    def test_to_dict_top_card_start_game(self):
        view_card = ViewCard(1, ("blue"))
        expected_dict = {
            "id": -1,
            "color_amount": 1,
            "color": ("blue",),
            "type": "number",
            "content": 1
        }
        actual_dict = view_card.to_dict_top_card()
        self.assertDictEqual(expected_dict, actual_dict)

    # Erste Karte im Ablagestapel: NumberCard
    # Zweite Karte im Ablagestapel: ViewCard
    def test_to_dict_top_card_mid_game_v1(self):
        first_top_card = NumberCard(1, (("blue"), ("red")), 2)
        second_top_card = ViewCard(2, ("green"))
        second_top_card.set_theoretical_card(first_top_card)
        expected_dict = {
            "id": -1,
            "color_amount": 2,
            "color": (("blue"), ("red")),
            "type": "number",
            "content": 2
        }
        actual_dict = second_top_card.to_dict_top_card()
        self.assertDictEqual(expected_dict, actual_dict)

    # Erste Karte im Ablagestapel: JokerCard
    # Zweite Karte im Ablagestapel: ViewCard
    def test_to_dict_top_card_mid_game_v2(self):
        first_top_card = JokerCard(1)
        second_top_card = ViewCard(2, ("green"))
        second_top_card.set_theoretical_card(first_top_card)
        expected_dict = {
            "id": -1,
            "color_amount": 4,
            "color": (("red"), ("blue"), ("yellow"), ("green")),
            "type": "number",
            "content": 1
        }
        actual_dict = second_top_card.to_dict_top_card()
        self.assertDictEqual(expected_dict, actual_dict)

    # Erste Karte im Ablagestapel: RestartCard
    # Zweite Karte im Ablagestapel: ViewCard
    def test_to_dict_top_card_mid_game_v3(self):
        first_top_card = RestartCard(1)
        second_top_card = ViewCard(2, ("green"))
        second_top_card.set_theoretical_card(first_top_card)
        expected_dict = {
            "id": -1,
            "color_amount": 4,
            "color": (("red"), ("blue"), ("yellow"), ("green")),
            "type": "number",
            "content": 1
        }
        actual_dict = second_top_card.to_dict_top_card()
        self.assertDictEqual(expected_dict, actual_dict)

    # Erste Karte im Ablagestapel: SelectionCard, einfarbig, no reference
    # Zweite Karte im Ablagestapel: ViewCard
    def test_to_dict_top_card_mid_game_v4_single_color_no_reference(self):
        first_top_card = SelectionCard(1, ("blue"))
        second_top_card = ViewCard(2, ("green"))
        second_top_card.set_theoretical_card(first_top_card)
        expected_dict = {
            "id": -1,
            "color_amount": 1,
            "color": ("blue",),
            "type": "number",
            "content": 1
        }
        actual_dict = second_top_card.to_dict_top_card()
        self.assertDictEqual(expected_dict, actual_dict)

    # Erste Karte im Ablagestapel: SelectionCard, vierfarbig, no reference
    # Zweite Karte im Ablagestapel: ViewCard
    def test_to_dict_top_card_mid_game_v4_four_color_no_reference(self):
        first_top_card = SelectionCard(1, (("red"), ("blue"), ("yellow"), ("green")))
        second_top_card = ViewCard(2, ("green"))
        second_top_card.set_theoretical_card(first_top_card)
        expected_dict = {
            "id": -1,
            "color_amount": 4,
            "color": (("red"), ("blue"), ("yellow"), ("green")),
            "type": "number",
            "content": 1
        }
        actual_dict = second_top_card.to_dict_top_card()
        self.assertDictEqual(expected_dict, actual_dict)

    # Erste Karte im Ablagestapel: SelectionCard, einfarbig, no reference
    # Zweite Karte im Ablagestapel: ViewCard
    def test_to_dict_top_card_mid_game_v4_single_color_with_reference(self):
        first_top_card = SelectionCard(1, ("blue"))
        first_top_card.set_theoretical_card(3)
        second_top_card = ViewCard(2, ("green"))
        second_top_card.set_theoretical_card(first_top_card)
        expected_dict = {
            "id": -1,
            "color_amount": 1,
            "color": ("blue",),
            "type": "number",
            "content": 3
        }
        actual_dict = second_top_card.to_dict_top_card()
        self.assertDictEqual(expected_dict, actual_dict)

    # Erste Karte im Ablagestapel: SelectionCard, vierfarbig, no reference
    # Zweite Karte im Ablagestapel: ViewCard
    def test_to_dict_top_card_mid_game_v4_four_color_with_reference(self):
        first_top_card = SelectionCard(1, (("red"), ("blue"), ("yellow"), ("green")))
        first_top_card.set_theoretical_card(2, ("red",))
        second_top_card = ViewCard(2, ("green"))
        second_top_card.set_theoretical_card(first_top_card)
        expected_dict = {
            "id": -1,
            "color_amount": 1,
            "color": ("red",),
            "type": "number",
            "content": 2
        }
        actual_dict = second_top_card.to_dict_top_card()
        self.assertDictEqual(expected_dict, actual_dict)

    # Erste Karte im Ablagestapel: ViewCard
    # Zweite Karte im Ablagestapel: ViewCard
    def test_to_dict_top_card_mid_game_v5(self):
        first_top_card = ViewCard(4, ("blue"))
        second_top_card = ViewCard(2, ("green"))
        second_top_card.set_theoretical_card(first_top_card)
        expected_dict = {
            "id": -1,
            "color_amount": 1,
            "color": ("blue",),
            "type": "number",
            "content": 1
        }
        actual_dict = second_top_card.to_dict_top_card()
        self.assertDictEqual(expected_dict, actual_dict)

"""
    # Erste Karte im Ablagestapel: ViewCard
    # Zweite Karte im Ablagestapel: ViewCard
    # Dritte Karte im Ablagestapel: ViewCard
    def test_to_dict_top_card_mid_game_v6(self):
        first_top_card = ViewCard(4, ("blue"))
        second_top_card = ViewCard(2, ("green"))
        second_top_card.set_theoretical_card(first_top_card)
        third_top_card = ViewCard(2, ("red"))
        third_top_card.set_theoretical_card(second_top_card)
        expected_dict = {
            "id": -1,
            "color_amount": 1,
            "color": ("blue",),
            "type": "number",
            "content": 1
        }
        actual_dict = third_top_card.to_dict_top_card()
        self.assertDictEqual(expected_dict, actual_dict)
"""


if __name__ == '__main__':
    unittest.main()
