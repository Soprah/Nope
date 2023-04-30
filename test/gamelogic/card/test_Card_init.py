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

    # Farbe doppelt
    def test_has_duplicate_color(self):
        with self.assertRaises(ValueError):
            Card(2, ("red", "red"))

    # Farbe ist in einem Tupel gespeichert
    def test_one_color_init_tuple(self):
        card = Card(1, self.color[0])
        self.assertIsInstance(card.color, tuple)

    # Keinen leeren String als Farbe übergeben
    def test_one_color_init_empty(self):
        with self.assertRaises(ValueError):
            card = Card(1, ())

    def test_one_color_init_empty(self):
        # Keinen leeren String als Farbe übergeben
        with self.assertRaises(ValueError):
            card = Card(1, ())

    def test_one_color_init_invalid(self):
        # Keine Zahl als Farbe übergeben
        with self.assertRaises(TypeError):
            card = Card(42)

    def test_one_color_init_amount_color(self):
        # Die Anzahl der Farben muss dem color_amount übereinstimmen
        card = Card(1, self.color[0])
        self.assertEqual(len(card.color), 1)


# Zweifarbige Karten
    def test_two_color_init_tuple(self):
        # Farbe ist in einem Tupel gespeichert
        card = Card(2, ("red", "blue"))
        self.assertIsInstance(card.color, tuple)

    def test_two_color_init_valid_color(self):
        # Gültige Farbe
        card = Card(2, ("red", "blue"))
        self.assertEqual(card.color, ("red", "blue"))

    def test_two_color_init_empty(self):
        # Keinen leeren String als Farbe übergeben
        with self.assertRaises(ValueError):
            card = Card(2, ())

    def test_two_color_init_invalid(self):
        # Keine Zahl als Farbe übergeben
        with self.assertRaises(TypeError):
            card = Card(42)

    def test_two_color_init_amount_color(self):
        # Die Anzahl der Farben muss dem color_amount übereinstimmen
        card = Card(2, ("red", "blue"))
        self.assertEqual(len(card.color), 2)

# Vierfarbige Karten
    def test_four_color_init_tuple(self):
        # Farbe ist in einem Tupel gespeichert
        card = Card(4, ("red", "blue", "yellow", "green"))
        self.assertIsInstance(card.color, tuple)

    def test_four_color_init_valid_color(self):
        # Gültige Farbe
        card = Card(4, ("red", "blue", "yellow", "green"))
        self.assertEqual(card.color, ("red", "blue", "yellow", "green"))

    def test_four_color_init_empty(self):
        # Keinen leeren String als Farbe übergeben
        with self.assertRaises(ValueError):
            card = Card(2, ())

    def test_four_color_init_invalid(self):
        # Keine Zahl als Farbe übergeben
        with self.assertRaises(TypeError):
            card = Card(42)

    def test_four_color_init_amount_color(self):
        # Die Anzahl der Farben muss dem color_amount übereinstimmen
        card = Card(4, ("red", "blue", "yellow", "green"))
        self.assertEqual(len(card.color), 4)


if __name__ == '__main__':
    unittest.main()
