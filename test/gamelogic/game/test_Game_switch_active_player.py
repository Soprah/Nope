import unittest

from src.gamelogic.game.Game import Game


class TestGameSwitchActivePlayer(unittest.TestCase):
    def setUp(self):
        self.game = Game("Eric", "Marc")


    def test_switch_active_player_game_start(self):
        self.assertEqual(self.game.active_player, self.game.player_1)

    def test_switch_active_player_first_switch(self):
        self.game.switch_active_player()
        self.assertEqual(self.game.active_player, self.game.player_2)

    """
    def test_switch_active_player_game_start(self):
        first_turn = self.game.next_turn()
        self.game.turns.append(first_turn)
        self.assertEqual(self.game.active_player, self.game.player_1)
    
    def test_switch_active_player(self):
    """

if __name__ == '__main__':
    unittest.main()
