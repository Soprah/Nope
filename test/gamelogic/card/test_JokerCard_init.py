import unittest

from src.gamelogic.card.JokerCard import JokerCard


class TestJokerCardInit(unittest.TestCase):
    def test_invalid_colors(self):
        with self.assertRaises(ValueError):
            invalid_colors = JokerCard(1, ("orange"))

    def test_valid_colors(self):
        j = JokerCard(1, (("red"), ("blue"), ("yellow"), ("green")))

if __name__ == '__main__':
    unittest.main()
