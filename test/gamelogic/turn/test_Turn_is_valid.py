import unittest

from src.gamelogic.card.NumberCard import NumberCard
from src.gamelogic.deck.Deck import Deck
from src.gamelogic.player.Player import Player
from src.gamelogic.turn.Turn import Turn


class TestTurnIsValid(unittest.TestCase):

    """
    HINWEIS:    "turn.is_valid"

                ⇾ prüft, ob ein Spielzug eines Spielers valide ist.

                :return: boolean
    """
    def setUp(self):
        self.deck = Deck()
        self.player = Player(self.deck, "eric")

    """ Der Spieler schickt eine leere Liste an Karten 
        und man hätte auch keinen Zug ausführen können """
    def test_is_valid_empty_selected_cards_true(self):
        card = NumberCard(49, ("green"), 1)
        turn = Turn(self.player, card)
        card1 = NumberCard(2, ("blue", "red"), 1)
        card2 = NumberCard(2, ("red", "blue"), 1)
        card3 = NumberCard(2, ("red", "yellow"), 1)
        self.player.hand = [card1, card2, card3]
        turn.possible_moves = turn.create_dict_possible_moves()
        self.assertTrue(turn.is_valid([]))

    """ Der Spieler schickt eine leere Liste an Karten 
        aber man hätte einen Zug ausführen können """
    def test_is_valid_empty_selected_cards_false(self):
        card = NumberCard(49, ("green"), 1)
        turn = Turn(self.player, card)
        card1 = NumberCard(2, ("blue", "red"), 1)
        card2 = NumberCard(8, ("red", "blue"), 1)
        card3 = NumberCard(9, ("green", "yellow"), 1)
        self.player.hand = [card1, card2, card3]
        turn.possible_moves = turn.create_dict_possible_moves()
        self.assertFalse(turn.is_valid([]))

    """ Der Spieler schickt eine Liste aus Karten, die er abwerfen möchte
        und es ist tatsächlich erlaubt """
    def test_is_valid_existing_selected_cards_one_choice_true(self):
        card = NumberCard(49, ("green"), 2)
        turn = Turn(self.player, card)
        card1 = NumberCard(2, ("blue", "red"), 1)
        card2 = NumberCard(8, ("red", "green"), 1)
        card3 = NumberCard(9, ("green", "yellow"), 1)
        self.player.hand = [card1, card2, card3]
        turn.possible_moves = turn.create_dict_possible_moves()
        self.assertTrue(turn.is_valid(selected_cards=[card2, card3]))

    def test_is_valid_existing_selected_cards_one_choice_false(self):
        card = NumberCard(49, ("blue"), 2)
        turn = Turn(self.player, card)
        card1 = NumberCard(2, ("blue", "red"), 1)
        card2 = NumberCard(8, ("red", "green"), 1)
        card3 = NumberCard(9, ("green", "yellow"), 1)
        self.player.hand = [card1, card2, card3]
        turn.possible_moves = turn.create_dict_possible_moves()
        self.assertFalse(turn.is_valid(selected_cards=[card1, card2]))

    def test_is_valid_existing_selected_cards_two_choice_true(self):
        card = NumberCard(49, ("green", "red"), 2)
        turn = Turn(self.player, card)
        card1 = NumberCard(2, ("blue", "red"), 1)
        card2 = NumberCard(8, ("green", "red"), 1)
        card3 = NumberCard(9, ("red"), 1)
        self.player.hand = [card1, card2, card3]
        turn.possible_moves = turn.create_dict_possible_moves()
        self.assertTrue(turn.is_valid(selected_cards=[card2, card3]))

    def test_is_valid_existing_selected_cards_two_choice_false(self):
        card = NumberCard(49, ("green", "red"), 2)
        turn = Turn(self.player, card)
        card1 = NumberCard(2, ("blue", "red"), 1)
        card2 = NumberCard(8, ("green", "red"), 1)
        card3 = NumberCard(9, ("yellow"), 1)
        self.player.hand = [card1, card2, card3]
        turn.possible_moves = turn.create_dict_possible_moves()
        self.assertFalse(turn.is_valid(selected_cards=[card2, card3]))


if __name__ == '__main__':
    unittest.main()
