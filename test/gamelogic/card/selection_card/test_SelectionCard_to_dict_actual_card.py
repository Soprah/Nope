import unittest

from src.gamelogic.card.SelectionCard import SelectionCard


class TestSelectionCardToDictActualCard(unittest.TestCase):
    def setUp(self):
        self.selection_card_single = SelectionCard(1, ("blue"))
        self.selection_card_multiple = SelectionCard(2, (("red"), ("blue"), ("green"), ("yellow")))

    # Einfarbige SelectionCard
    def test_to_dict_actual_card_single_color(self):
        expected_dict = {
            "id": 1,
            "color_amount": 1,
            "color": ("blue",),
            "type": "action",
            "content": "selection",
        }
        actual_dict = self.selection_card_single.to_dict_actual_card()
        self.assertDictEqual(expected_dict, actual_dict)

    # Vierfarbige SelectionCard
    def test_to_dict_actual_card_four_color(self):
        expected_dict = {
            "id": 2,
            "color_amount": 4,
            "color": (("red"), ("blue"), ("green"), ("yellow")),
            "type": "action",
            "content": "selection",
        }
        actual_dict = self.selection_card_multiple.to_dict_actual_card()
        self.assertDictEqual(expected_dict, actual_dict)
if __name__ == '__main__':
    unittest.main()