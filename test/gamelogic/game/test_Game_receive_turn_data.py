import unittest

from src.gamelogic.game.Game import Game


class TestGameReceiveTurnData(unittest.TestCase):

    def setUp(self):
        self.game = Game("eric", "marc")

    """ Prüft, ob die empfangenen Karten, die der Spieler abwerfen möchte, gültig sind.
        - Nicht vorhandene IDs """
    def test_receive_turn_data_invalid_ids_not_exist(self):
        player_selected_cards_id = [
            self.game.active_player.hand[0].id,
            123,
            self.game.active_player.hand[2].id,
        ]
        sent_dict_cards = {"id": player_selected_cards_id}
        with self.assertRaises(ValueError):
            received_cards = self.game.receive_turn_data(sent_dict_cards)

    """ Prüft, ob die empfangenen Karten, die der Spieler abwerfen möchte, gültig sind.
            - Doppelte IDs """
    def test_receive_turn_data_invalid_ids_double(self):
        player_selected_cards_id = [
            self.game.active_player.hand[0].id,
            self.game.active_player.hand[0].id,
            self.game.active_player.hand[2].id,
        ]
        sent_dict_cards = {"id": player_selected_cards_id}
        with self.assertRaises(ValueError):
            received_cards = self.game.receive_turn_data(sent_dict_cards)


    """ Prüft, ob die empfangenen Karten, die der Spieler abwerfen möchte, gültig sind.
        - Gültige IDs """
    def test_receive_turn_data_valid_ids_existing_list(self):
        # Spieler wählt Karten aus
        player_selected_cards_id = [
            self.game.active_player.hand[0].id,
            self.game.active_player.hand[1].id,
            self.game.active_player.hand[2].id,
        ]
        sent_dict_cards = {"id": player_selected_cards_id}
        # Funktion ordnet die ids den Deck-karten zu und erstellt eine Liste aus den Deck-karten
        received_cards = self.game.receive_turn_data(sent_dict_cards)
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
        sent_dict_cards = {"id": player_selected_cards_id}
        received_cards = self.game.receive_turn_data(sent_dict_cards)
        self.assertEqual(len(received_cards), 0)






if __name__ == '__main__':
    unittest.main()