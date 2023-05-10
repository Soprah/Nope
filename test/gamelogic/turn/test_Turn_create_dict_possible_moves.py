import unittest

from src.gamelogic.card.NumberCard import NumberCard
from src.gamelogic.deck.Deck import Deck
from src.gamelogic.player.Player import Player
from src.gamelogic.turn.Turn import Turn


class TestTurnCreateDictPossibleMoves(unittest.TestCase):

    """
    HINWEIS:    "turn.create_dict_possible_moves"

                ⇾ Benötigt Dictionary (key=color, value=cards)
                von "turn.get_cards_matching_color"
                ⇾ Benötigt einen boolean (genügend Karten für Spielzug)
                von "turn.has_sufficient_matching_cards"

                erstellt ein finales dictionary aus keys mit Karten
    """
    def setUp(self):
        self.deck = Deck()
        self.player = Player(self.deck, "eric")

    """ Spieler kann bei einer einfarbigen top_card keinen gültigen Zug ausführen """
    def test_create_dict_possible_moves_one_color_no_list(self):
        card = NumberCard(49, ("green"), 1)
        turn = Turn(self.player, card)
        card1 = NumberCard(2, ("blue", "red"), 1)
        card2 = NumberCard(2, ("red", "blue"), 1)
        card3 = NumberCard(2, ("red", "yellow"), 1)
        self.player.hand = [card1, card2, card3]
        actual_possible_moves = turn.create_dict_possible_moves()
        expected_possible_moves = {}
        self.assertEqual(actual_possible_moves, expected_possible_moves)

    """ Spieler kann bei einer einfarbigen top_card einen gültigen Zug machen """
    def test_create_dict_possible_moves_one_color_one_list(self):
        card = NumberCard(1, ("blue"), 2)
        turn = Turn(self.player, card)
        card1 = NumberCard(2, ("blue", "red"), 1)
        card2 = NumberCard(2, ("red", "blue"), 1)
        card3 = NumberCard(2, ("green", "yellow"), 1)
        self.player.hand = [card1, card2, card3]
        expected_possible_moves = {"blue": [card1, card2]}
        actual_possible_moves = turn.create_dict_possible_moves()
        self.assertEqual(expected_possible_moves, actual_possible_moves)

    """ Spieler kann bei einer zweifarbigen top_card keinen gültigen Zug machen """
    def test_create_dict_possible_moves_two_color_no_list(self):
        card = NumberCard(49, ("green", "yellow"), 2)
        turn = Turn(self.player, card)
        card1 = NumberCard(28, ("blue", "red"), 1)
        card2 = NumberCard(9, ("red", "blue"), 1)
        card3 = NumberCard(65, ("yellow"), 1)
        self.player.hand = [card1, card2, card3]
        actual_possible_moves = turn.create_dict_possible_moves()
        expected_possible_moves = {}
        self.assertEqual(actual_possible_moves, expected_possible_moves)

    """ Spieler kann bei einer zweifarbigen top_card einen gültigen Zug machen """
    def test_create_dict_possible_moves_two_colors_one_list(self):
        card = NumberCard(2, ("blue", "green"), 2)
        turn = Turn(self.player, card)
        card1 = NumberCard(2, ("blue", "red"), 1)
        card2 = NumberCard(2, ("red", "blue"), 1)
        card3 = NumberCard(2, ("green", "yellow"), 1)
        self.player.hand = [card1, card2, card3]
        expected_possible_moves = {"blue": [card1, card2]}
        actual_possible_moves = turn.create_dict_possible_moves()
        self.assertEqual(expected_possible_moves, actual_possible_moves)

    """ Spieler kann bei einer zweifarbigen top_card zwei gültige Zug machen """
    def test_create_dict_possible_moves_two_colors_two_lists(self):
        card = NumberCard(2, ("blue", "green"), 2)
        turn = Turn(self.player, card)
        card1 = NumberCard(2, ("blue", "red"), 1)
        card2 = NumberCard(2, ("green", "blue"), 1)
        card3 = NumberCard(2, ("green", "yellow"), 1)
        self.player.hand = [card1, card2, card3]
        expected_possible_moves = {"blue": [card1, card2], "green": [card2, card3]}
        actual_possible_moves = turn.create_dict_possible_moves()
        self.assertEqual(expected_possible_moves, actual_possible_moves)

    def test_create_dict_possible_moves_two_colors_two_lists_v2(self):
        card = NumberCard(49, ("green", "red"), 2)
        turn = Turn(self.player, card)
        card1 = NumberCard(2, ("blue", "red"), 1)
        card2 = NumberCard(8, ("red", "green"), 1)
        card3 = NumberCard(9, ("green"), 1)
        self.player.hand = [card1, card2, card3]
        expected_possible_moves = {"green": [card2, card3], "red": [card1, card2]}
        actual_possible_moves = turn.create_dict_possible_moves()
        self.assertEqual(expected_possible_moves, actual_possible_moves)


if __name__ == '__main__':
    unittest.main()
