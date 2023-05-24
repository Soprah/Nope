import unittest

from src.gamelogic.card.JokerCard import JokerCard

class TestJokerCardInit(unittest.TestCase):

    def test_valid_colors(self):
        colors = (("red"), ("blue"), ("yellow"), ("green"))
        j = JokerCard(1)
        for i in range(len(colors)):
            self.assertEqual(j.color[i], colors[i])

if __name__ == '__main__':
    unittest.main()