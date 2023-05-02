import unittest

from src.gamelogic.card.NumberCard import NumberCard


class TestNumberCard(unittest.TestCase):
    def test_init_valid_number(self):
        ncard1 = NumberCard(1, ("red"), 1, 1)
        ncard2 = NumberCard(1, ("red"), 2, 2)
        ncard3 = NumberCard(1, ("red"), 3, 3)

    def test_init_invalid_number(self):
        with self.assertRaises(ValueError):
            ncard = NumberCard(1, ("red"), 1, 4)


if __name__ == '__main__':
    unittest.main()
