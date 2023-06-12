import unittest

from src.gamelogic.card.RestartCard import RestartCard

class TestRestartCardInit(unittest.TestCase):

    def test_valid_colors(self):
        colors = (("red"), ("blue"), ("yellow"), ("green"))
        r = RestartCard(1)
        for i in range(len(colors)):
            self.assertEqual(r.color[i], colors[i])

if __name__ == '__main__':
    unittest.main()