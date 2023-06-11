import unittest

from src.gamelogic.card.NumberCard import NumberCard
from src.gamelogic.deck.Deck import Deck
from src.gamelogic.game.Game import Game
from src.gamelogic.player.Player import Player
from src.gamelogic.turn.Turn import Turn


class TestTurnIsValid(unittest.TestCase):

    """
    HINWEIS:    "turn.is_valid"

                ⇾ prüft, ob ein Spielzug eines Spielers valide ist.

                :return: boolean
    """
    def setUp(self):

        # Alte Tests
        self.deck = Deck()
        self.player = Player(self.deck, "eric")

        # Neue Tests

        # Spielvorbereitung
        self.p1 = Player("Christina", 8)
        self.p2 = Player("Marc", 19)
        self.game = Game(self.p1, self.p2)

        # Karten
        self.g_1 = self.game.deck.cards_dict.get(5)
        self.y_1 = self.game.deck.cards_dict.get(7)
        self.b_1 = self.game.deck.cards_dict.get(4)
        self.view_red = self.game.deck.cards_dict.get(91)
        self.y_3 = self.game.deck.cards_dict.get(20)
        self.g_2 = self.game.deck.cards_dict.get(14)
        self.y_2 = self.game.deck.cards_dict.get(16)
        self.selection_blue = self.game.deck.cards_dict.get(96)



# ALTE TESTS

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

# NEUE TESTS

    # FIRST ATTEMPT - MUST PLAY
    def test_is_valid_case_A_1(self):
        p1_hand = [
            self.g_1,
            self.y_1,
            self.b_1,
            self.view_red,
            self.y_3,
            self.g_2,
            self.y_2,
            self.selection_blue
        ]

        # Vorbereitungen
        r_1 = self.game.deck.cards_dict.get(1)
        top_card = r_1
        turn = Turn(self.p1, top_card)
        self.p1.hand = p1_hand
        possible_cards_to_play = [self.view_red]
        impossible_cards_to_play = [self.y_1]

        # Funktion
        turn.possible_moves = turn.create_dict_possible_moves()

        # Test

        # Dictionary prüfen
        self.assertTrue(turn.player_has_set())
        self.assertTrue(len(turn.possible_moves) == 1)
        self.assertTrue(len(turn.possible_moves.get("red")) == 1)
        self.assertEqual(self.view_red, turn.possible_moves.get("red")[0])

        # is_valid
        self.assertTrue(turn.is_valid(possible_cards_to_play))
        self.assertFalse(turn.is_valid(impossible_cards_to_play))

    # FIRST ATTEMPT - CAN PLAY
    # def test_is_valid_case_A_2(self):
    #     p1_hand = [
    #         self.g_1,
    #         self.y_1,
    #         self.b_1,
    #         self.view_red,
    #         self.y_3,
    #         self.g_2,
    #         self.y_2,
    #         self.selection_blue
    #     ]
    #
    #     # Vorbereitungen
    #     r_2 = self.game.deck.cards_dict.get(9)
    #     top_card = r_2
    #     turn = Turn(self.p1, top_card)
    #     self.p1.hand = p1_hand
    #     possible_set_to_play = []
    #     possible_action_card_to_play = [self.view_red]
    #     impossible_cards_to_play = [self.y_1]
    #
    #     # Funktion
    #     turn.possible_moves = turn.create_dict_possible_moves()
    #
    #     # Test
    #
    #     # Dictionary prüfen
    #     self.assertFalse(turn.player_has_set())
    #     self.assertTrue(len(turn.possible_moves) == 0)
    #
    #     # is_valid
    #     self.assertTrue(turn.is_valid(possible_action_card_to_play))
    #     # self.assertFalse(turn.is_valid(impossible_cards_to_play))

    '''
    def is_valid(self, selected_cards):
        """
        Überprüft, ob die übergebenen Karten einen gültigen Spielzug darstellen

        :param selected_cards: Liste an Karten, die der Spieler für einen Spielzug ausgesucht hat
        :return: boolean
        """
        self.turn_attempt = self.turn_attempt + 1
        self.selected_cards = selected_cards
        self.possible_moves = self.create_dict_possible_moves()
        if len(selected_cards) == 0:
            self.is_turn_valid = self.player_has_set() == False and len(selected_cards) == 0
        elif len(selected_cards) > 0:
            self.is_turn_valid = self.selected_cards_represent_set(selected_cards)
        if self.is_turn_valid == False:
            self.player.is_disqualified = True
        return self.is_turn_valid
    '''

if __name__ == '__main__':
    unittest.main()
