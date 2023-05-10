import unittest

from src.gamelogic.card.NumberCard import NumberCard
from src.gamelogic.deck.Deck import Deck
from src.gamelogic.player.Player import Player
from src.gamelogic.turn.Turn import Turn


class TestTurnHasSufficientMatchingCards(unittest.TestCase):

    """
    HINWEIS:    "turn.has_sufficient_matching_cards"

                ⇾ Benötigt Dictionary (key=color, value=cards)
                von "turn.get_cards_matching_color"

                prüft nur, ob es für einen key genügend Karten gibt.
                :return: boolean
    """

    def setUp(self):
        self.deck = Deck()
        self.player = Player(self.deck, "eric")

    """ Spieler hat genügend Karten einer Farbe für einen validen Zug """
    def test_has_sufficient_matching_cards_two_color_one_list_true(self):
        card = NumberCard(2, ("blue", "green"), 2)
        turn = Turn(self.player, card)
        card1 = NumberCard(2, ("blue", "red"), 1)
        card2 = NumberCard(2, ("red", "blue"), 1)
        card3 = NumberCard(2, ("green", "yellow"), 1)
        self.player.hand = [card1, card2, card3]
        expected_boolean = True
        turn.possible_moves = turn.get_cards_matching_color()
        actual_boolean = turn.has_sufficient_matching_cards("blue")
        self.assertEqual(actual_boolean, expected_boolean)

    """ Spieler besitzt nicht genügend Karten einer Farbe für einen validen Zug """
    def test_has_sufficient_matching_cards_two_color_one_list_false(self):
        card = NumberCard(2, ("yellow", "green"), 2)
        turn = Turn(self.player, card)
        card1 = NumberCard(2, ("blue", "red"), 1)
        card2 = NumberCard(2, ("red", "blue"), 1)
        card3 = NumberCard(2, ("green", "yellow"), 1)
        self.player.hand = [card1, card2, card3]
        expected_boolean = False
        turn.possible_moves = turn.get_cards_matching_color()
        actual_boolean = turn.has_sufficient_matching_cards("yellow")
        self.assertEqual(actual_boolean, expected_boolean)


if __name__ == '__main__':
    unittest.main()
