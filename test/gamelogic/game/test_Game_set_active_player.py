import unittest

from src.gamelogic.game.Game import Game


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.player_1_name = "Eric"
        self.player_2_name = "Marc"

    def test_set_active_player_game_start(self):
        game = Game(self.player_1_name, self.player_2_name)
        self.assertEqual(game.active_player, game.player_1)
        game.set_active_player()
        self.assertEqual(game.active_player, game.player_1)


if __name__ == '__main__':
    unittest.main()
