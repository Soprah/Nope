import unittest

from src.gamelogic.game.Game import Game
from src.gamelogic.player.Player import Player
from src.gamelogic.dataconvert.DataConvert import DataConvert


class TestNetToGamelogic(unittest.TestCase):

    def setUp(self):
        self.player_1_name = "Eric"
        self.player_1_id = 1
        self.player_2_name = "Marc"
        self.player_2_id = 2
        self.p1 = Player(self.player_1_name, self.player_1_id)
        self.p2 = Player(self.player_2_name, self.player_2_id)
        self.game = Game(self.p1, self.p2)

        self.dc = DataConvert()

    """ Spieler schickt leere Liste """
    def test_net_to_gamelogic_empty_id_list(self):
        player_selected_cards_id = []
        sent_dict_cards = {
            "selected_cards": player_selected_cards_id,
            "token": self.player_1_id
        }
        expected_output_dict = {
            "selected_cards": player_selected_cards_id,
            "token": self.player_1_id,
            "game": self.game
        }

        actual_output_dict = self.dc.net_to_gamelogic(sent_dict_cards, self.game)
        self.assertDictEqual(expected_output_dict, actual_output_dict)

    """ Prüft, ob die empfangenen Karten, die der Spieler abwerfen möchte, gültig sind.
            - Nicht vorhandene IDs """
    def test_net_to_gamelogic_invalid_ids_not_exist_in_game(self):
        player_selected_cards_id = [
            self.game.active_player.hand[0].id,
            123,
            self.game.active_player.hand[2].id,
        ]
        sent_dict_cards = {
            "selected_cards": player_selected_cards_id,
            "token": self.player_1_id,
        }

        actual_output = self.dc.net_to_gamelogic(sent_dict_cards, self.game)
        self.assertTrue(self.game.player_1.is_disqualified)
        self.assertEqual("ID existiert nicht in der Spielerhand", self.game.reason_of_disqualification)

    """ Prüft, ob die empfangenen Karten, die der Spieler abwerfen möchte, gültig sind.
            - Doppelte IDs """
    def test_net_to_gamelogic_invalid_ids_double(self):
        player_selected_cards_id = [
            self.game.active_player.hand[0].id,
            self.game.active_player.hand[0].id,
            self.game.active_player.hand[2].id,
        ]
        sent_dict_cards = {
            "selected_cards": player_selected_cards_id,
            "token": self.player_1_id
        }
        output_dict = self.dc.net_to_gamelogic(sent_dict_cards, self.game)
        self.assertTrue(self.game.player_1.is_disqualified)
        self.assertEqual("Die IDs enthalten Duplikate", self.game.reason_of_disqualification)


    """ Prüft, ob die empfangenen Karten, die der Spieler abwerfen möchte, gültig sind.
        - Gültige IDs """
    def test_net_to_gamelogic_valid_ids_existing_list(self):
        # Spieler wählt Karten aus
        player_selected_cards_id = [
            self.game.active_player.hand[0].id,
            self.game.active_player.hand[1].id,
            self.game.active_player.hand[2].id,
        ]

        # Client Dictionary
        sent_dict_cards = {
            "selected_cards": player_selected_cards_id,
            "token": self.player_1_id
        }

        # Funktion ordnet die ids den Deck-karten zu und erstellt eine Liste aus den Deck-karten
        output_dict = self.dc.net_to_gamelogic(sent_dict_cards, self.game)
        received_cards = output_dict.get("selected_cards")

        # Prüfen, ob es die Karte im Deck gibt
        for card in received_cards:

            # Gibt es die karte überhaupt im Deck
            self.assertIn(card, self.game.deck.cards)

            # Gibt/Gab es die Karte in der Spielerhand
            self.assertIn(card, self.game.active_player.hand)

        expected_cards = [
            self.game.active_player.hand[0],
            self.game.active_player.hand[1],
            self.game.active_player.hand[2],
        ]

        self.assertEqual(len(received_cards), 3)
        self.assertEqual(received_cards, expected_cards)

        # Richtige Anzahl an Schlüsseln im output dictionary
        self.assertTrue(len(output_dict) == 3)

        # Beinhaltet das output dictionary das game object
        self.assertIsNotNone(output_dict.get("game"))
        self.assertEqual(output_dict.get("game"), self.game)

    """ Prüft den Spezialfall einer einfarbigen Selection Card
        - Gültige Wahlwerte """

### SELECTION CARD CASE

# SINGLE COLOR

    # GÜLTIG
    def test_net_to_gamelogic_single_color_selection_card_valid_choice(self):
        # color=green
        selection_card = self.game.deck.cards_dict.get(97)
        self.p1.hand = [selection_card]
        selected_id_cards = [selection_card.id]
        input = {
            "token": self.player_1_id,
            "selected_cards": selected_id_cards,
            "chosen_number": 3
        }
        expected_output = {
            "token": self.player_1_id,
            "selected_cards": [selection_card],
            "game": self.game
        }

        actual_output = self.dc.net_to_gamelogic(input, self.game)

        # Gleiches Dictionary
        self.assertEqual(expected_output, actual_output)

        # Wahlwerte wurden gesetzt
        edited_card = actual_output.get("selected_cards")[0]
        actual_number = edited_card.get_number()
        self.assertEqual(3, actual_number)

    # UNGÜLTIG
    def test_net_to_gamelogic_single_color_selection_card_invalid_choice(self):
        # color=green der selection_card
        selection_card = self.game.deck.cards_dict.get(97)
        self.p1.hand = [selection_card]
        selected_id_cards = [selection_card.id]
        input_dict = {
            "token": self.player_1_id,
            "selected_cards": selected_id_cards,
            "chosen_number": 7
        }
        # expected_output = {
        #     "token": self.player_1_id,
        #     "selected_cards": [selection_card],
        #     "game": self.game
        # }

        actual_output = self.dc.net_to_gamelogic(input_dict, self.game)

        # Gleiches Dictionary
        # self.assertEqual(expected_output, actual_output)

        # Spieler disqualifiziert
        self.assertTrue(self.game.active_player.is_disqualified)
        self.assertEqual(self.game.reason_of_disqualification,
        "Es wurden falsche Wahlwerte für die einfarbige SelectionCard übergeben")

    # FEHLT
    def test_net_to_gamelogic_single_color_selection_card_missing_choice(self):
        # color=green der selection_card
        selection_card = self.game.deck.cards_dict.get(97)
        self.p1.hand = [selection_card]
        selected_id_cards = [selection_card.id]
        input_dict = {
            "token": self.player_1_id,
            "selected_cards": selected_id_cards,
        }
        # expected_output = {
        #     "token": self.player_1_id,
        #     "selected_cards": [selection_card],
        #     "game": self.game
        # }
        actual_output = self.dc.net_to_gamelogic(input_dict, self.game)
        # Gleiches Dictionary
        # self.assertEqual(expected_output, actual_output)

        # Spieler disqualifiziert
        self.assertTrue(self.game.active_player.is_disqualified)
        self.assertEqual(self.game.reason_of_disqualification, "Der Schlüssel 'chosen_number' befand sich nicht im dictionary")


# FOUR COLOR

    # GÜLTIG
    def test_net_to_gamelogic_four_color_selection_card_valid_choice(self):
        # SelectionCard: id=100, color=(("red"), ("blue"), ("yellow"), ("green"))
        selection_card = self.game.deck.cards_dict.get(100)
        self.p1.hand = [selection_card]
        selected_id_cards = [selection_card.id]
        input_dict = {
            "token": self.player_1_id,
            "selected_cards": selected_id_cards,
            "chosen_number": 3,
            "chosen_color": ("blue",)
        }
        expected_output = {
            "token": self.player_1_id,
            "selected_cards": [selection_card],
            "game": self.game
        }

        actual_output = self.dc.net_to_gamelogic(input_dict, self.game)

        # Gleiches Dictionary
        self.assertEqual(expected_output, actual_output)

        # Spieler nicht disqualifiziert
        self.assertFalse(self.game.active_player.is_disqualified)

        # Wahlwerte wurden gesetzt
        edited_card = actual_output.get("selected_cards")[0]
        actual_number = edited_card.get_number()
        actual_color = edited_card.get_color()
        self.assertEqual(3, actual_number)
        self.assertEqual(("blue",), actual_color)

    # UNGÜLTIG - Zahl
    def test_net_to_gamelogic_four_color_selection_card_invalid_number_choice(self):
        # SelectionCard: id=100, color=(("red"), ("blue"), ("yellow"), ("green"))
        selection_card = self.game.deck.cards_dict.get(100)
        self.p1.hand = [selection_card]
        selected_id_cards = [selection_card.id]
        input_dict = {
            "token": self.player_1_id,
            "selected_cards": selected_id_cards,
            "chosen_number": 4,
            "chosen_color": ("blue",)
        }
        expected_output = {
            "token": self.player_1_id,
            "selected_cards": [selection_card],
            "game": self.game
        }

        actual_output = self.dc.net_to_gamelogic(input_dict, self.game)

        # Gleiches Dictionary
        # self.assertEqual(expected_output, actual_output)

        # Spieler nicht disqualifiziert
        self.assertTrue(self.game.active_player.is_disqualified)

        # Wahlwerte wurden nicht gesetzt
        edited_card = actual_output.get("selected_cards")[0]
        actual_number = edited_card.get_number()
        actual_color = edited_card.get_color()
        self.assertEqual(1, actual_number)
        self.assertEqual((("red"), ("blue"), ("yellow"), ("green")), actual_color)

    # UNGÜLTIG - Farbe
    def test_net_to_gamelogic_four_color_selection_card_invalid_color_choice(self):
        # SelectionCard: id=100, color=(("red"), ("blue"), ("yellow"), ("green"))
        selection_card = self.game.deck.cards_dict.get(100)
        self.p1.hand = [selection_card]
        selected_id_cards = [selection_card.id]
        input_dict = {
            "token": self.player_1_id,
            "selected_cards": selected_id_cards,
            "chosen_number": 3,
            "chosen_color": ("purple",)
        }
        expected_output = {
            "token": self.player_1_id,
            "selected_cards": [selection_card],
            "game": self.game
        }

        actual_output = self.dc.net_to_gamelogic(input_dict, self.game)

        # Gleiches Dictionary
        # self.assertEqual(expected_output, actual_output)

        # Spieler nicht disqualifiziert
        self.assertTrue(self.game.active_player.is_disqualified)

        # Wahlwerte wurden nicht gesetzt
        edited_card = actual_output.get("selected_cards")[0]
        actual_number = edited_card.get_number()
        actual_color = edited_card.get_color()
        self.assertEqual(1, actual_number)
        self.assertEqual((("red"), ("blue"), ("yellow"), ("green")), actual_color)

    # FEHLT - Zahl
    def test_net_to_gamelogic_four_color_selection_card_missing_number_choice(self):
        # SelectionCard: id=100, color=(("red"), ("blue"), ("yellow"), ("green"))
        selection_card = self.game.deck.cards_dict.get(100)
        self.p1.hand = [selection_card]
        selected_id_cards = [selection_card.id]
        input_dict = {
            "token": self.player_1_id,
            "selected_cards": selected_id_cards,
            # "chosen_number": 3,
            "chosen_color": ("blue",)
        }
        expected_output = {
            "token": self.player_1_id,
            "selected_cards": [selection_card],
            "game": self.game
        }

        actual_output = self.dc.net_to_gamelogic(input_dict, self.game)

        # Gleiches Dictionary
        # self.assertEqual(expected_output, actual_output)

        # Spieler nicht disqualifiziert
        self.assertTrue(self.game.active_player.is_disqualified)

        # Wahlwerte wurden nicht gesetzt
        edited_card = actual_output.get("selected_cards")[0]
        actual_number = edited_card.get_number()
        actual_color = edited_card.get_color()
        self.assertEqual(1, actual_number)
        self.assertEqual((("red"), ("blue"), ("yellow"), ("green")), actual_color)

    # FEHLT - Farbe
    def test_net_to_gamelogic_four_color_selection_card_missing_number_choice(self):
        # SelectionCard: id=100, color=(("red"), ("blue"), ("yellow"), ("green"))
        selection_card = self.game.deck.cards_dict.get(100)
        self.p1.hand = [selection_card]
        selected_id_cards = [selection_card.id]
        input_dict = {
            "token": self.player_1_id,
            "selected_cards": selected_id_cards,
            "chosen_number": 3,
            # "chosen_color": ("blue",)
        }
        expected_output = {
            "token": self.player_1_id,
            "selected_cards": [selection_card],
            "game": self.game
        }

        actual_output = self.dc.net_to_gamelogic(input_dict, self.game)

        # Gleiches Dictionary
        # self.assertEqual(expected_output, actual_output)

        # Spieler nicht disqualifiziert
        self.assertTrue(self.game.active_player.is_disqualified)

        # Wahlwerte wurden nicht gesetzt
        edited_card = actual_output.get("selected_cards")[0]
        actual_number = edited_card.get_number()
        actual_color = edited_card.get_color()
        self.assertEqual(1, actual_number)
        self.assertEqual((("red"), ("blue"), ("yellow"), ("green")), actual_color)

if __name__ == '__main__':
    unittest.main()
