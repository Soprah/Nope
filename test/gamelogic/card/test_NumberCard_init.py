import unittest

from src.gamelogic.card.NumberCard import NumberCard


class NumberCardTest(unittest.TestCase):
    def test_init_valid_number(self):
        ncard1 = NumberCard(5, ("red"), 1)
        ncard2 = NumberCard(9, ("red"), 2)
        ncard3 = NumberCard(56, ("red"), 3)

    def test_init_invalid_number(self):
        with self.assertRaises(ValueError):
            ncard = NumberCard(21, ("red"), 7)


if __name__ == '__main__':
    unittest.main()
