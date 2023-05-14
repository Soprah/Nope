import unittest

from src.gamelogic.player.Player import Player
from src.gamemanagement.GameManagement import GameManagement


class GameManagementAssignPlayerToGame(unittest.TestCase):

    def setUp(self):
        self.gm = GameManagement()

    def test_assign_player_to_game_correct_id(self):
        player_1_id = 1
        player_2_id = 2
        player_1_name = "Eric"
        player_2_name = "Marc"
        self.gm.assign_player_to_game(player_1_id, player_1_name, player_2_id, player_2_name)

        game_1 = self.gm.game_sessions.get(player_1_id)
        game_2 = self.gm.game_sessions.get(player_2_id)

        self.assertIsNotNone(game_1)
        self.assertIsNotNone(game_2)
        self.assertIs(game_1, game_2)

        self.assertEqual(player_1_id, game_1.player_1.id)
        self.assertEqual(player_2_id, game_1.player_2.id)

    def test_assign_player_to_game_correct_id_multiple_games(self):
        player_1_id = 1
        player_2_id = 2
        player_1_name = "Eric"
        player_2_name = "Marc"
        self.gm.assign_player_to_game(player_1_id, player_1_name, player_2_id, player_2_name)
        player_3_id = 3
        player_4_id = 4
        player_3_name = "Rainer"
        player_4_name = "Sabine"
        self.gm.assign_player_to_game(player_3_id, player_3_name, player_4_id, player_4_name)

        game_1 = self.gm.game_sessions.get(player_3_id)
        game_2 = self.gm.game_sessions.get(player_4_id)

        self.assertIsNotNone(game_1)
        self.assertIsNotNone(game_2)
        self.assertIs(game_1, game_2)

if __name__ == '__main__':
    unittest.main()
