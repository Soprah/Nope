import unittest

from src.gamelogic.game.Game import Game
from src.gamelogic.player.Player import Player
from src.gamelogic.turn.Turn import Turn


class TestGameSendTurnData(unittest.TestCase):
    def setUp(self):
        self.p1 = Player("Eric", 3)
        self.p2 = Player("Marc", 19)
        self.game = Game(self.p1, self.p2)

    def test_send_turn_data_game_start(self):
        # turn = Turn(self.game.active_player, self.game.deck.discard_stack[-1])
        turn = self.game.next_turn()
        actual_turn_data = self.game.send_turn_data(current_turn=turn)
        self.assertEqual(actual_turn_data.get("previous_selected_cards"), [])
        self.assertEqual(actual_turn_data.get("top_card"), self.game.deck.discard_stack[-1])
        self.assertEqual(actual_turn_data.get("amount_opponent_cards"), len(self.game.player_2.hand))
        self.assertEqual(actual_turn_data.get("own_hand_cards"), self.game.player_1.hand)

    """ MUSS NOCH IMPLEMENTIERT WERDEN """
    # def test_send_turn_data_mid_game(self):
    #     pass

if __name__ == '__main__':
    unittest.main()
