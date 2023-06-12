import unittest

from src.gamelogic.card.SelectionCard import SelectionCard


class TestSelectionCardSetTheoreticalCard(unittest.TestCase):
    def setUp(self):
        self.selection_card_single = SelectionCard(1, ("blue"))
        self.selection_card_multiple = SelectionCard(2, (("red"), ("blue"), ("green"), ("yellow"),))

        self.number_choice = 2
        self.color_choice = ("red")

    # Instanziierung: Nur Zahl
    def test_set_theoretical_card_only_number(self):
        self.selection_card_single.set_theoretical_card(self.number_choice)

        self.assertEqual(self.selection_card_single.theoretical_card.number, self.number_choice)

    # Instannziierung: Zahl und Farbe
    def test_set_theoretical_card_number_and_color(self):
        self.selection_card_multiple.set_theoretical_card(self.number_choice, self.color_choice)

        self.assertEqual(self.selection_card_multiple.theoretical_card.number, self.number_choice)
        self.assertEqual(self.selection_card_multiple.theoretical_card.color, self.color_choice)

    # Instanziierung: Zahl / Zahl und Farbe bei vorhandenem Verweis
    def test_set_theoretical_card_with_exisiting_reference(self):
        self.selection_card_single.set_theoretical_card(self.number_choice)
        with self.assertRaises(ValueError):
            self.selection_card_single.set_theoretical_card(self.number_choice)

        self.selection_card_multiple.set_theoretical_card(self.number_choice, self.color_choice)
        with self.assertRaises(ValueError):
            self.selection_card_multiple.set_theoretical_card(self.number_choice, self.color_choice)


if __name__ == '__main__':
    unittest.main()