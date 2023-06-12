import unittest

from src.gamelogic.card.ViewCard import ViewCard


class TestViewCardToDictActualCard(unittest.TestCase):
    def setUp(self):
        self.view_card = ViewCard(76, ("yellow"))

    def test_to_dict_actual_card(self):
        expected_dict = {
            "id": 76,
            "color_amount": 1,
            "color": ("yellow",),
            "type": "action",
            "content": "view",
        }
        actual_dict = self.view_card.to_dict_actual_card()
        self.assertDictEqual(expected_dict, actual_dict)

if __name__ == '__main__':
    unittest.main()
