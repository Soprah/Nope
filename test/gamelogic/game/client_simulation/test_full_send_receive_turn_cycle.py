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
        first_turn = self.game.next_turn()
        self.assertEqual(first_turn.top_card, self.game.deck.discard_stack[-1])
        self.assertEqual(len(self.game.deck.discard_stack), 1)
        self.assertEqual(len(self.game.active_player.hand), 8)
        for card in self.game.active_player.hand:
            self.assertIsInstance(card, Card)

        turn_data = self.game.send_turn_data(first_turn)
        self.assertIsInstance(turn_data, dict)
        self.assertEqual(len(turn_data), 3)
        self.assertEqual(turn_data.get("previous_selected_cards"), first_turn.top_card)
        self.assertEqual(turn_data.get("amount_opponent_cards"), 8)
        self.assertEqual(turn_data.get("own_hand_cards"), self.game.active_player.hand)

        client_processed_data = self.game.active_player.CS_select_cards(turn_data)
        self.assertTrue(len(client_processed_data) == 1 or len(client_processed_data) == 2)

        checked_list_with_ids = self.game.receive_turn_data(client_processed_data)
        self.assertTrue(first_turn.is_valid(checked_list_with_ids))


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