import unittest

from src.gamelogic.card.SelectionCard import SelectionCard


class TestSelectionCardToDictTopCard(unittest.TestCase):
    def setUp(self):
        self.selection_card_single = SelectionCard(1, ("blue"))
        self.selection_card_multiple = SelectionCard(2, (("red"), ("blue"), ("green"), ("yellow")))

        self.number_choice = 2
        self.color_choice = ("red")

    # Anfang des Spiels / Keine theoretical card Referenz - einfarbige SelectionCard
    def test_to_dict_top_card_single_color_start_game(self):
        expected_dict = {
            "id": -1,
            "color_amount": 1,
            "color": ("blue",),
            "type": "number",
            "content": 1
        }
        actual_dict = self.selection_card_single.to_dict_top_card()
        self.assertDictEqual(expected_dict, actual_dict)

    # Anfang des Spiels / Keine theoretical card Referenz - vierfarbige SelectionCard
    def test_to_dict_top_card_four_color_start_game(self):
        expected_dict = {
            "id": -1,
            "color_amount": 4,
            "color": (("red"), ("blue"), ("green"), ("yellow")),
            "type": "number",
            "content": 1
        }
        actual_dict = self.selection_card_multiple.to_dict_top_card()
        self.assertDictEqual(expected_dict, actual_dict)

    # Während des Spiels / Vorhandene theoretical card Referenz - einfarbige SelectionCard
    def test_to_dict_top_card_single_color_mid_game(self):
        self.selection_card_single.set_theoretical_card(self.number_choice)
        expected_dict = {
            "id": -1,
            "color_amount": 1,
            "color": ("blue",),
            "type": "number",
            "content": self.number_choice
        }
        actual_dict = self.selection_card_single.to_dict_top_card()
        self.assertDictEqual(expected_dict, actual_dict)

    # Während des Spiels / Vorhandene theoretical card Referenz - vierfarbige SelectionCard
    def test_to_dict_top_card_four_color_mid_game(self):
        self.selection_card_multiple.set_theoretical_card(self.number_choice)
        expected_dict = {
            "id": -1,
            "color_amount": 4,
            "color": (("red"), ("blue"), ("green"), ("yellow")),
            "type": "number",
            "content": self.number_choice
        }
        actual_dict = self.selection_card_multiple.to_dict_top_card()
        self.assertDictEqual(expected_dict, actual_dict)


if __name__ == '__main__':
    unittest.main()
