import unittest

from src.gamelogic.card.ViewCard import ViewCard


class TestViewCardInit(unittest.TestCase):
    def test_invalid_colors(self):
        with self.assertRaises(ValueError):
            invalid_colors_card = ViewCard(1, ("orange"))


if __name__ == '__main__':
    unittest.main()
