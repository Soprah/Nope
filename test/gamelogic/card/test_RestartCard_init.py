import unittest

from src.gamelogic.card.RestartCard import RestartCard


class TestRestartCardInit(unittest.TestCase):
    def test_invalid_colors(self):
        with self.assertRaises(ValueError):
            invalid_colors_card = RestartCard(1, ("red"))
        


if __name__ == '__main__':
    unittest.main()