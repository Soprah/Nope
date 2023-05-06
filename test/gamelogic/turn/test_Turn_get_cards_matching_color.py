import unittest

from src.gamelogic.card.NumberCard import NumberCard
from src.gamelogic.deck.Deck import Deck
from src.gamelogic.player.Player import Player
from src.gamelogic.turn.Turn import Turn


class TestTurnGetCardsMatchingColor(unittest.TestCase):

    """
    HINWEIS:    "turn.get_cards_matching_color"

                prüft nur, ob ein Spieler überhaupt Karten einer geforderten Farbe besitzt.
                prüft NICHT, ob die Anzahl der Karten ausreicht, die er für einen validen Zug benötigt!

                Einordnung: Erster Schritt vor der nächsten Funktion "turn.has_sufficient_matching_cards"
    """
    def setUp(self):
        self.deck = Deck()
        self.player = Player(self.deck, "eric")
        self.first_top_card = self.deck.initialize_discard_stack()

    """ Spieler hat keine Karten in der geforderten Farbe """
    def test_get_cards_matching_color_one_color_no_list(self):
        card = NumberCard(1, ("green"), 2)
        turn = Turn(self.player, card)
        card1 = NumberCard(2, ("blue", "red"), 1)
        card2 = NumberCard(2, ("red", "blue"), 1)
        card3 = NumberCard(2, ("red", "yellow"), 1)
        self.player.hand = [card1, card2, card3]
        expected_dict = {"green": []}
        turn.possible_moves = turn.get_cards_matching_color()
        self.assertEqual(turn.possible_moves, expected_dict)

    """ Spieler besitzt Karten in der geforderten Farbe """
    def test_get_cards_matching_color_one_color_one_list(self):
        card = NumberCard(1, ("blue"), 2)
        turn = Turn(self.player, card)
        card1 = NumberCard(2, ("blue", "red"), 1)
        card2 = NumberCard(2, ("red", "blue"), 1)
        card3 = NumberCard(2, ("green", "yellow"), 1)
        self.player.hand = [card1, card2, card3]
        expected_dict = {"blue": [card1, card2]}
        turn.possible_moves = turn.get_cards_matching_color()
        self.assertEqual(turn.possible_moves, expected_dict)

    """ Spieler hat bei einer zweifarbigen top_card keine Karten 
            der geforderten Farbe """
    def test_get_cards_matching_color_two_colors_no_list(self):
        card = NumberCard(2, ("yellow", "green"), 2)
        turn = Turn(self.player, card)
        card1 = NumberCard(2, ("blue", "red"), 1)
        card2 = NumberCard(2, ("red", "blue"), 3)
        card3 = NumberCard(2, ("red", "blue"), 2)
        self.player.hand = [card1, card2, card3]
        expected_dict = {"yellow": [], "green": []}
        turn.possible_moves = turn.get_cards_matching_color()
        self.assertEqual(turn.possible_moves, expected_dict)

    """ Spieler besitzt bei einer zweifarbigen top_card Karten
            von einer geforderten Farbe """
    def test_get_cards_matching_color_two_colors_one_list(self):
        card = NumberCard(2, ("blue", "green"), 2)
        turn = Turn(self.player, card)
        card1 = NumberCard(2, ("blue", "red"), 1)
        card2 = NumberCard(2, ("red", "blue"), 1)
        card3 = NumberCard(2, ("red", "yellow"), 1)
        self.player.hand = [card1, card2, card3]
        expected_dict = {"blue": [card1, card2], "green": []}
        turn.possible_moves = turn.get_cards_matching_color()
        self.assertEqual(turn.possible_moves, expected_dict)

    """ Spieler besitzt bei einer zweifarbigen top_card Karten
                von beiden geforderten Farben """
    def test_get_cards_matching_color_two_colors_two_lists(self):
        card = NumberCard(2, ("blue", "green"), 2)
        turn = Turn(self.player, card)
        card1 = NumberCard(2, ("blue", "red"), 1)
        card2 = NumberCard(2, ("red", "blue"), 1)
        card3 = NumberCard(2, ("green", "yellow"), 1)
        self.player.hand = [card1, card2, card3]
        expected_dict = {"blue": [card1, card2], "green": [card3]}
        turn.possible_moves = turn.get_cards_matching_color()
        self.assertEqual(turn.possible_moves, expected_dict)

if __name__ == '__main__':
    unittest.main()
