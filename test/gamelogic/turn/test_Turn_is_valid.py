import unittest

from src.dataconvert.DataConvert import DataConvert
from src.gamelogic.card.NumberCard import NumberCard
from src.gamelogic.card.SelectionCard import SelectionCard
from src.gamelogic.card.ViewCard import ViewCard
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
        self.dc = DataConvert()

        # Karten
        self.g_1 = self.game.deck.cards_dict.get(5)
        self.y_1 = self.game.deck.cards_dict.get(7)
        self.b_1 = self.game.deck.cards_dict.get(4)
        self.view_red = self.game.deck.cards_dict.get(91)
        # self.view_red.clear_theoretical_card()
        self.y_3 = self.game.deck.cards_dict.get(20)
        self.g_2 = self.game.deck.cards_dict.get(14)
        self.y_2 = self.game.deck.cards_dict.get(16)
        self.selection_blue = self.game.deck.cards_dict.get(96)

        self.g_3 = self.game.deck.cards_dict.get(19)
        self.b_3 = self.game.deck.cards_dict.get(18)
        self.multi_sel = self.game.deck.cards_dict.get(100)


    def tearDown(self):
        self.view_red = None



# ALTE TESTS - ZAHLENKARTEN

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
        card4 = NumberCard(9, ("blue", "green"), 1)
        self.player.hand = [card1, card2, card3, card4]
        turn.possible_moves = turn.create_dict_possible_moves()
        self.assertTrue(len(turn.possible_moves) == 2)
        self.assertTrue(turn.is_valid(selected_cards=[card2, card3]))
        self.assertTrue(turn.is_valid(selected_cards=[card2, card1]))

    def test_is_valid_existing_selected_cards_two_choice_false(self):
        card = NumberCard(49, ("green", "red"), 2)
        turn = Turn(self.player, card)
        card1 = NumberCard(2, ("blue", "red"), 1)
        card2 = NumberCard(8, ("green", "red"), 1)
        card3 = NumberCard(9, ("yellow"), 1)
        self.player.hand = [card1, card2, card3]
        turn.possible_moves = turn.create_dict_possible_moves()
        self.assertFalse(turn.is_valid(selected_cards=[card2, card3]))

# NEUE TESTS, Ergänzung zu oben mit Aktionskarten

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
        nope = []
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
        self.assertFalse(turn.is_valid(nope))

    # FIRST ATTEMPT - CAN PLAY | SECOND ATTEMPT - MUST PLAY
    def test_is_valid_case_A_2(self):
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
        r_2 = self.game.deck.cards_dict.get(9)
        top_card = r_2
        turn = Turn(self.p1, top_card)
        self.p1.hand = p1_hand
        nope = []
        possible_action_card_to_play = [self.view_red]
        impossible_cards_to_play = [self.y_1]

        # Funktion
        turn.possible_moves = turn.create_dict_possible_moves()

        # Test

        # Dictionary prüfen
        self.assertFalse(turn.player_has_set())
        self.assertTrue(len(turn.possible_moves) == 0)

        # is_valid
        self.assertTrue(turn.is_valid(possible_action_card_to_play))
        self.assertFalse(turn.is_valid(impossible_cards_to_play))
        self.assertTrue(turn.is_valid(nope))

        ## ZWEITER VERSUCH

        # Vorbereitungen
        r_1 = self.game.deck.cards_dict.get(1)
        r_3 = self.game.deck.cards_dict.get(17)
        self.p1.hand.append(r_1)
        self.p1.hand.append(r_3)
        nope = []
        possible_set_to_play_only_numbers = [r_1, r_3]
        possible_set_to_play_including_action = [r_1, self.view_red]
        impossible_cards_to_play = [self.g_2]

        # Funktion
        turn.possible_moves = turn.create_dict_possible_moves()

        # Dictionary prüfen
        self.assertTrue(turn.player_has_set())
        self.assertTrue(len(turn.possible_moves) == 1)

        # is_valid
        self.assertTrue(turn.is_valid(possible_action_card_to_play))
        self.assertTrue(turn.is_valid(possible_set_to_play_only_numbers))
        self.assertTrue(turn.is_valid(possible_set_to_play_including_action))
        self.assertFalse(turn.is_valid(impossible_cards_to_play))
        self.assertFalse(turn.is_valid(nope))

    # FIRST ATTEMPT - CAN PLAY | SECOND ATTEMPT - CAN PLAY
    def test_is_valid_case_A_3(self):
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
        r_2 = self.game.deck.cards_dict.get(9)
        top_card = r_2
        turn = Turn(self.p1, top_card)
        self.p1.hand = p1_hand
        nope = []
        possible_action_card_to_play = [self.view_red]
        impossible_cards_to_play = [self.y_1]

        # Funktion
        turn.possible_moves = turn.create_dict_possible_moves()

        # Test

        # Dictionary prüfen
        self.assertFalse(turn.player_has_set())
        self.assertTrue(len(turn.possible_moves) == 0)

        # is_valid
        self.assertTrue(turn.is_valid(possible_action_card_to_play))
        self.assertFalse(turn.is_valid(impossible_cards_to_play))
        self.assertTrue(turn.is_valid(nope))

        ## ZWEITER VERSUCH

        # Vorbereitungen
        r_1 = self.game.deck.cards_dict.get(1)
        b_2 = self.game.deck.cards_dict.get(11)
        self.p1.hand.append(r_1)
        self.p1.hand.append(b_2)
        nope = []
        possible_set_to_play_including_action = [r_1, self.view_red]
        impossible_cards_to_play = [b_2]

        # Funktion
        turn.possible_moves = turn.create_dict_possible_moves()

        # Dictionary prüfen
        self.assertTrue(turn.player_has_set())
        self.assertTrue(len(turn.possible_moves) == 1)

        # is_valid
        self.assertTrue(turn.is_valid(possible_action_card_to_play))
        self.assertTrue(turn.is_valid(possible_set_to_play_including_action))
        self.assertFalse(turn.is_valid(impossible_cards_to_play))
        self.assertFalse(turn.is_valid(nope))

    # TOP_CARD = VIEW als Startkarte
    def test_is_valid_case_A_6(self):
        p1_hand = [
            self.g_1,
            self.y_1,
            self.b_1,
            self.g_3,
            self.y_3,
            self.g_2,
            self.y_2,
            self.selection_blue
        ]
        self.assertIsInstance(self.view_red, ViewCard)


        # Vorbereitungen
        top_card = self.view_red
        self.game.deck.discard_stack[0] = top_card
        turn = self.game.next_turn()
        self.p1.hand = p1_hand
        nope = []
        impossible_cards_to_play = [self.y_1]

        # ViewCard Wert prüfen
        self.assertEqual(1, self.view_red.get_number())
        self.assertEqual(("red",), self.view_red.get_color())
        self.assertIsInstance(self.view_red, ViewCard)

        # Funktion
        turn.possible_moves = turn.create_dict_possible_moves()

        # Test

        # Dictionary prüfen
        self.assertFalse(turn.player_has_set())
        self.assertTrue(len(turn.possible_moves) == 0)

        # is_valid
        self.assertFalse(turn.is_valid(impossible_cards_to_play))
        self.assertTrue(turn.is_valid(nope))

        ## ZWEITER VERSUCH

        # Vorbereitungen
        r_1 = self.game.deck.cards_dict.get(1)
        b_2 = self.game.deck.cards_dict.get(11)
        self.p1.hand.append(r_1)
        self.p1.hand.append(b_2)
        nope = []
        possible_set_to_play = [r_1]
        impossible_cards_to_play = [b_2]

        # Funktion
        turn.possible_moves = turn.create_dict_possible_moves()

        # Dictionary prüfen
        self.assertTrue(turn.player_has_set())
        self.assertTrue(len(turn.possible_moves) == 1)

        # is_valid
        self.assertTrue(turn.is_valid(possible_set_to_play))
        self.assertFalse(turn.is_valid(impossible_cards_to_play))
        self.assertFalse(turn.is_valid(nope))
        # """

    # TOP_CARD = VIEW mit unterer Karte (gelbe=2)
    def test_is_valid_case_A_7(self):
        selected_id_cards = [self.view_red.id]
        first_turn_dict = {
            "token": self.p1.id,
            "selected_cards": selected_id_cards
        }

        # First Turn Vorbereitungen
        self.p1.hand = [self.view_red]
        first_turn = self.game.next_turn()
        # top_card = numbercard, number=2, color=("yellow",)
        first_turn.top_card = self.game.deck.cards_dict.get(15)

        # Data wird verarbeitet
        processed_first_turn = self.dc.net_to_gamelogic(first_turn_dict, self.game)

        # ViewCard Werte übernommen?
        processed_vc = processed_first_turn.get("selected_cards")[0]
        self.assertEqual(processed_vc, self.view_red)
        number = processed_vc.get_number()
        color = processed_vc.get_color()
        self.assertEqual(2, number)
        self.assertEqual(("yellow",), color)

        # Karte "künstlich" ablegen
        self.game.deck.discard_stack[-1] = processed_vc


        # Second Turn Vorbereitungen
        second_turn = self.game.next_turn()

        r_1 = self.game.deck.cards_dict.get(1)
        p2_hand = [
            self.g_1,
            self.y_1,
            self.b_1,
            self.g_3,
            self.y_3,
            self.g_2,
            self.y_2,
            self.selection_blue,
            r_1
        ]

        self.p2.hand = p2_hand
        nope = []
        possible_cards_to_play_v1 = [self.y_1, self.y_2]
        possible_cards_to_play_v2 = [self.y_1, self.y_3]
        possible_cards_to_play_v3 = [self.y_2, self.y_3]
        impossible_cards_to_play = [r_1]

        # Top Card nochmal überprüfen
        self.assertEqual(2, self.view_red.get_number())
        self.assertEqual(("yellow",), self.view_red.get_color())
        self.assertIsInstance(self.view_red, ViewCard)

        # Funktion
        second_turn.possible_moves = second_turn.create_dict_possible_moves()

        # Test

        # Dictionary prüfen
        self.assertTrue(len(second_turn.possible_moves) == 1)
        self.assertTrue(second_turn.player_has_set())

        # is_valid
        self.assertFalse(second_turn.is_valid(impossible_cards_to_play))
        self.assertFalse(second_turn.is_valid(nope))
        self.assertTrue(second_turn.is_valid(possible_cards_to_play_v1))
        self.assertTrue(second_turn.is_valid(possible_cards_to_play_v2))
        self.assertTrue(second_turn.is_valid(possible_cards_to_play_v3))

    # TOP_CARD = SELECTION als Startkarte
    def test_is_valid_case_A_8(self):
        p1_hand = [
            self.g_1,
            self.y_1,
            self.b_1,
            self.g_3,
            self.y_3,
            self.g_2,
            self.y_2,
            self.view_red
        ]

        # Vorbereitungen
        # TODO
        top_card = self.selection_blue
        self.game.deck.discard_stack[0] = top_card
        turn = self.game.next_turn()
        self.p1.hand = p1_hand
        nope = []
        possible_set_to_play = [self.b_1]
        impossible_cards_to_play = [self.y_1]

        # SelectionCard Wert prüfen
        self.assertEqual(1, self.selection_blue.get_number())
        self.assertEqual(("blue",), self.selection_blue.get_color())
        self.assertIsInstance(self.selection_blue, SelectionCard)

        # Funktion
        turn.possible_moves = turn.create_dict_possible_moves()

        # Test

        # Dictionary prüfen
        self.assertTrue(turn.player_has_set())
        self.assertTrue(len(turn.possible_moves) == 1)

        # is_valid
        self.assertFalse(turn.is_valid(impossible_cards_to_play))
        self.assertFalse(turn.is_valid(nope))
        self.assertTrue(possible_set_to_play)

    # TOP_CARD = SINGLE SEL mit Wahlwerte
    def test_is_valid_case_A_9(self):
        selected_id_cards = [self.selection_blue.id]
        first_turn_dict = {
            "token": self.p1.id,
            "selected_cards": selected_id_cards,
            "chosen_number": 2
        }

        # First Turn Vorbereitungen
        self.p1.hand = [self.selection_blue]
        first_turn = self.game.next_turn()
        # top_card = numbercard, number=1, color=("blue",)
        first_turn.top_card = self.game.deck.cards_dict.get(4)

        # Data wird verarbeitet
        processed_first_turn = self.dc.net_to_gamelogic(first_turn_dict, self.game)

        # Wahlwerte übernommen?
        processed_vc = processed_first_turn.get("selected_cards")[0]
        self.assertEqual(processed_vc, self.selection_blue)
        number = processed_vc.get_number()
        self.assertEqual(2, number)
        self.assertEqual(("blue",), self.selection_blue.get_color())

        # Karte "künstlich" ablegen
        self.game.deck.discard_stack[-1] = processed_vc


        # Second Turn Vorbereitungen
        second_turn = self.game.next_turn()

        r_1 = self.game.deck.cards_dict.get(1)
        p2_hand = [
            self.g_1,
            self.y_1,
            self.b_1,
            self.g_3,
            self.y_3,
            self.g_2,
            self.y_2,
            self.b_3,
        ]

        self.p2.hand = p2_hand
        nope = []
        possible_cards_to_play = [self.b_3, self.b_1]
        impossible_cards_to_play = [self.b_1]

        # Top Card nochmal überprüfen
        self.assertEqual(2, self.selection_blue.get_number())
        self.assertEqual(("blue",), self.selection_blue.get_color())
        self.assertIsInstance(self.selection_blue, SelectionCard)

        # Funktion
        second_turn.possible_moves = second_turn.create_dict_possible_moves()

        # Test

        # Dictionary prüfen
        self.assertTrue(len(second_turn.possible_moves) == 1)
        self.assertTrue(second_turn.player_has_set())

        # is_valid
        self.assertFalse(second_turn.is_valid(impossible_cards_to_play))
        self.assertFalse(second_turn.is_valid(nope))
        self.assertTrue(second_turn.is_valid(possible_cards_to_play))

    # TOP_CARD = MULTIPLE SEL mit Wahlwerte
    def test_is_valid_case_A_10(self):
        selected_id_cards = [self.multi_sel.id]
        first_turn_dict = {
            "token": self.p1.id,
            "selected_cards": selected_id_cards,
            "chosen_number": 2,
            "chosen_color": ("green",)
        }

        # First Turn Vorbereitungen
        self.p1.hand = [self.multi_sel]
        first_turn = self.game.next_turn()
        # top_card = numbercard, number=1, color=("blue",)
        first_turn.top_card = self.game.deck.cards_dict.get(4)

        # Data wird verarbeitet
        processed_first_turn = self.dc.net_to_gamelogic(first_turn_dict, self.game)

        # Wahlwerte übernommen?
        processed_vc = processed_first_turn.get("selected_cards")[0]
        self.assertEqual(processed_vc, self.multi_sel)
        number = processed_vc.get_number()
        self.assertEqual(2, number)
        self.assertEqual(("green",), self.multi_sel.get_color())

        # Karte "künstlich" ablegen
        self.game.deck.discard_stack[-1] = processed_vc


        # Second Turn Vorbereitungen
        second_turn = self.game.next_turn()

        r_1 = self.game.deck.cards_dict.get(1)
        p2_hand = [
            self.g_1,
            self.y_1,
            self.b_1,
            self.g_3,
            self.y_3,
            self.g_2,
            self.y_2,
            self.b_3,
        ]

        self.p2.hand = p2_hand
        nope = []
        possible_cards_to_play_v1 = [self.g_1, self.g_2]
        possible_cards_to_play_v2 = [self.g_2, self.g_3]
        possible_cards_to_play_v3 = [self.g_3, self.g_1]
        impossible_cards_to_play = [self.b_1]

        # Top Card nochmal überprüfen
        self.assertEqual(2, self.multi_sel.get_number())
        self.assertEqual(("green",), self.multi_sel.get_color())
        self.assertIsInstance(self.multi_sel, SelectionCard)

        # Funktion
        second_turn.possible_moves = second_turn.create_dict_possible_moves()

        # Test

        # Dictionary prüfen
        self.assertTrue(len(second_turn.possible_moves) == 1)
        self.assertTrue(second_turn.player_has_set())

        # is_valid
        self.assertFalse(second_turn.is_valid(impossible_cards_to_play))
        self.assertFalse(second_turn.is_valid(nope))
        self.assertTrue(second_turn.is_valid(possible_cards_to_play_v1))
        self.assertTrue(second_turn.is_valid(possible_cards_to_play_v2))
        self.assertTrue(second_turn.is_valid(possible_cards_to_play_v3))

if __name__ == '__main__':
    unittest.main()
