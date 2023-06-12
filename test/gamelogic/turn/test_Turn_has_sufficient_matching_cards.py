import unittest

from src.gamelogic.card.JokerCard import JokerCard
from src.gamelogic.card.NumberCard import NumberCard
from src.gamelogic.card.SelectionCard import SelectionCard
from src.gamelogic.card.ViewCard import ViewCard
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

    # NumberCards
    def test_has_sufficient_matching_cards_two_color_one_list(self):
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

    # ActionCards & NumberCards | NC top card
    def test_has_sufficient_matching_cards_two_color_one_list_v1(self):
        card = NumberCard(2, ("blue", "green"), 2)
        turn = Turn(self.player, card)
        card1 = NumberCard(2, ("blue", "red"), 1)
        card2 = JokerCard(2)
        card3 = NumberCard(2, ("green", "yellow"), 1)
        self.player.hand = [card1, card2, card3]
        expected_boolean = True
        turn.possible_moves = turn.get_cards_matching_color()
        actual_boolean = turn.has_sufficient_matching_cards("blue")
        self.assertEqual(actual_boolean, expected_boolean)

    # ActionCards & NumberCards | AC top card
    def test_has_sufficient_matching_cards_four_color_one_list_v2(self):
        card = JokerCard(2)
        turn = Turn(self.player, card)
        card1 = ViewCard(2, ("blue"))
        self.player.hand = [card1]
        expected_boolean = True
        turn.possible_moves = turn.get_cards_matching_color()
        actual_boolean = turn.has_sufficient_matching_cards("blue")
        self.assertEqual(actual_boolean, expected_boolean)


    """ Spieler besitzt nicht genügend Karten einer Farbe für einen validen Zug """

    # NumberCards
    def test_has_sufficient_matching_cards_two_color_no_list(self):
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

    # ActionCards & NumberCards | NC top card
    def test_has_sufficient_matching_cards_two_color_no_list_v1(self):
        card = NumberCard(2, ("blue", "green"), 2)
        turn = Turn(self.player, card)
        card1 = NumberCard(2, ("blue", "red"), 1)
        card2 = SelectionCard(2, ("yellow"))
        card3 = NumberCard(2, ("green", "yellow"), 1)
        self.player.hand = [card1, card2, card3]
        turn.possible_moves = turn.get_cards_matching_color()
        actual_boolean = turn.has_sufficient_matching_cards("blue")
        self.assertFalse(actual_boolean)

# NOTIZ
# Folgende Fälle fehlen noch
# SelectionCard: Wo die Zahl (und die Farbe) ausgesucht werden muss
# ViewCard: Wo die Karte unter der ViewCard relevant ist

    # ActionCards & NumberCards | AC top card
    '''
    def test_has_sufficient_matching_cards_one_color_no_list_v2(self):
        card = SelectionCard(2, ("blue", "green"))
        turn = Turn(self.player, card)
        card1 = NumberCard(2, ("blue", "red"), 1)
        card2 = SelectionCard(2, ("yellow"))
        card3 = NumberCard(2, ("green", "yellow"), 1)
        self.player.hand = [card1, card2, card3]
        turn.possible_moves = turn.get_cards_matching_color()
        actual_boolean = turn.has_sufficient_matching_cards("blue")
        self.assertFalse(actual_boolean)
    '''

if __name__ == '__main__':
    unittest.main()