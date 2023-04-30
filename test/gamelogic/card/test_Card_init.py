import unittest

from src.gamelogic.Card import Card

class MyTestCase(unittest.TestCase):


    def setUp(self):
        self.color = [("red"), ("blue"), ("yellow"), ("green")]

# Einfarbige Karten

    # Gültige Farbe
    def test_invalid_color(self):
        with self.assertRaises(ValueError):
            card = Card(1, ("purple"))

    # Farbe ist in einem Tupel gespeichert
    def test_one_color_init_tuple(self):
        card = Card(self.color[0])
        self.assertIsInstance(card.color, tuple)

    # Keinen leeren String als Farbe übergeben
    def test_one_color_init_empty(self):
        with self.assertRaises(ValueError):
            card = Card(1, ())

if __name__ == '__main__':
    unittest.main()
