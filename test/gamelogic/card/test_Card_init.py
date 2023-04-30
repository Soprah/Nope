import unittest

from src.gamelogic.Card import Card

class MyTestCase(unittest.TestCase):


    def setUp(self):
        self.color = [("red"), ("blue"), ("yellow"), ("green")]

# Einfarbige Karten

    def test_invalid_color(self):
        with self.assertRaises(ValueError):
            card = Card(("purple"))


if __name__ == '__main__':
    unittest.main()
