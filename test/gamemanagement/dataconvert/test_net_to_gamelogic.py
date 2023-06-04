import unittest

from src.gamelogic.game.Game import Game
from src.gamelogic.player.Player import Player
from src.gamemanagement.DataConvert import DataConvert


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

    """ Prüft, ob die empfangenen Karten, die der Spieler abwerfen möchte, gültig sind.
            - Nicht vorhandene IDs """
    def test_net_to_gamelogic_invalid_ids_not_exist(self):
        player_selected_cards_id = [
            self.game.active_player.hand[0].id,
            123,
            self.game.active_player.hand[2].id,
        ]
        sent_dict_cards = {
            "selected_cards": player_selected_cards_id,
            "token": self.player_1_id
        }
        output_dict = self.dc.net_to_gamelogic(sent_dict_cards, self.game)
        self.assertTrue(self.game.player_1.is_disqualified)
        self.assertEqual(self.game.reason_of_disqualification, f"Die Karte mit der id 123 existiert nicht"
                                            f" in der Hand des Spielers, der die Karte geschickt hat")

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
        self.assertTrue(self.game.player_1.is_disqualified or self.game.player_2.is_disqualified)
        self.assertEqual(self.game.reason_of_disqualification, "Die IDs enthalten Duplikate")

    """ Prüft, ob die empfangenen Karten, die der Spieler abwerfen möchte, gültig sind.
        - Gültige IDs """
    def test_receive_turn_data_valid_ids_existing_list(self):
        # Spieler wählt Karten aus
        player_selected_cards_id = [
            self.game.active_player.hand[0].id,
            self.game.active_player.hand[1].id,
            self.game.active_player.hand[2].id,
        ]
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

    """ Prüft, ob die empfangenen Karten, die der Spieler abwerfen möchte, gültig sind.
        - Keine IDs """
    def test_receive_turn_data_no_ids(self):
        player_selected_cards_id = []
        sent_dict_cards = {
            "selected_cards": player_selected_cards_id,
            "token": self.player_1_id
        }
        output_dict = self.dc.net_to_gamelogic(sent_dict_cards, self.game)
        received_cards = output_dict.get("selected_cards")
        self.assertEqual(len(received_cards), 0)

if __name__ == '__main__':
    unittest.main()
