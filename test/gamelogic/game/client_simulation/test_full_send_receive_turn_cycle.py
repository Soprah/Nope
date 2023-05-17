import unittest

from src.gamelogic.card.Card import Card
from src.gamelogic.game.Game import Game
from src.gamelogic.player.Player import Player
from src.gamelogic.turn.Turn import Turn


class TestSendReceiveTurnCycle(unittest.TestCase):

    def setUp(self):
        p1 = Player("Eric", 1)
        p2 = Player("Marc", 2)
        self.game = Game(p1, p2)

    def test_game_start_full_cycle_valid_cards(self):
        # Spielzug erstellen
        first_turn = self.game.next_turn()
        self.assertEqual(first_turn.top_card, self.game.deck.discard_stack[-1])
        self.assertEqual(len(self.game.deck.discard_stack), 1)
        self.assertEqual(len(self.game.active_player.hand), 8)
        for card in self.game.active_player.hand:
            self.assertIsInstance(card, Card)

        # Spielzugdaten verpacken & senden
        turn_data = self.game.send_turn_data(first_turn)
        self.assertIsInstance(turn_data, dict)
        self.assertEqual(len(turn_data), 4)
        self.assertEqual(turn_data.get("previous_selected_cards"), [])
        self.assertEqual(turn_data.get("top_card"), first_turn.top_card)
        self.assertEqual(turn_data.get("amount_opponent_cards"), 8)
        self.assertEqual(turn_data.get("own_hand_cards"), self.game.active_player.hand)

        # Client verarbeitet Spielzugdaten & schickt Ergebnis
        client_processed_data = self.game.active_player.CS_select_cards(turn_data)
        self.assertTrue(len(client_processed_data) == 1 or len(client_processed_data) == 2)

        # Server erhält Daten & prüft Validität
        checked_list_with_ids = self.game.receive_turn_data(client_processed_data)
        is_first_turn_valid = first_turn.is_valid(checked_list_with_ids)
        self.assertTrue(is_first_turn_valid)

        # Prüfen, ob der Spieler noch einen Versuch starten muss
        if is_first_turn_valid and first_turn.is_another_attempt_necessary():

            # Spieler zieht zwei neue Karten
            player_card_amount = len(self.game.active_player.hand)
            self.game.active_player.draw_card()
            self.game.active_player.draw_card()
            self.assertEqual(len(self.game.active_player.hand), player_card_amount + 2)

            # Server verpackt & sendet erneut Spielzugdaten
            second_turn_data = self.game.send_turn_data(first_turn)
            self.assertIsInstance(second_turn_data, dict)
            self.assertEqual(len(second_turn_data), 4)
            self.assertEqual(second_turn_data.get("previous_selected_cards"), [])
            self.assertEqual(second_turn_data.get("top_card"), first_turn.top_card)
            self.assertEqual(second_turn_data.get("amount_opponent_cards"), 10)
            self.assertEqual(second_turn_data.get("own_hand_cards"), self.game.active_player.hand)

            # Client verarbeitet Spielzugdaten & schickt Ergebnis
            client_processed_data = self.game.active_player.CS_select_cards(turn_data)
            self.assertTrue(len(client_processed_data) == 1 or len(client_processed_data) == 2)

            # Server erhält Daten & prüft Validität für den zweiten Versuch
            second_checked_list_with_ids = self.game.receive_turn_data(client_processed_data)
            second_is_first_turn_valid = first_turn.is_valid(second_checked_list_with_ids)
            self.assertTrue(second_is_first_turn_valid)

            # Zweiter Versuch des Clients
            if second_is_first_turn_valid:
                old_top_card = first_turn.top_card
                discarded_cards = self.game.make_move()

                # Spieler konnte wieder keine Karten ablegen
                if len(discarded_cards) == 0:
                    self.assertEqual(first_turn.top_card, self.game.deck.discard_stack[0])

                # Spieler konnte tatsächlich Karten ablegen
                else:
                    
                    new_top_card = first_turn.selected_cards[-1]
                    self.assertNotEqual(new_top_card, old_top_card)
                    self.assertEqual(new_top_card, discarded_cards[-1])



    def test_mid_game_full_cycle_valid_cards(self):
        first_turn = self.game.next_turn()
        # turn_data

if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestSendReceiveTurnCycle)
    #
    # # Anzahl der Durchläufe festlegen
    # num_runs = 500
    #
    # # Schleife, die den Test mehrmals ausführt
    # for i in range(num_runs):
    #     print("Durchlauf Nr.", i + 1)
    #     unittest.TextTestRunner().run(suite)
    #     print()

