import unittest

from src.gamelogic.card.RestartCard import RestartCard


class TestRestartCardInit(unittest.TestCase):
    def test_invalid_colors(self):
        with self.assertRaises(ValueError):
            invalid_colors_card = RestartCard(1, ("red"))
        
    def test_correct_colors(self):
        restart_card = RestartCard(1, (("red"), ("blue"), ("yellow"), ("green")))

if __name__ == '__main__':
    unittest.main()