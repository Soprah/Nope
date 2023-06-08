import unittest

from src.gamelogic.game.Game import Game
from src.gamelogic.player.Player import Player


class TestGameGetPlayerViaId(unittest.TestCase):

    def setUp(self):
        self.p1 = Player("Eric", 33)
        self.p2 = Player("Marc", 99)
        self.game = Game(self.p1, self.p2)

    # Player 1 - ID für Player 1 - Richtig
    def test_get_player_via_id_player1_right_id(self):
        player = self.game.get_player_via_id(33)
        self.assertEqual(self.p1, player)

    # Player 1 - ID für Player 2 - Falsch
    def test_get_player_via_id_player1_wrong_id(self):
        player = self.game.get_player_via_id(99)
        self.assertNotEqual(self.p1, player)

    # Player 1 - random ID  - Falsch
    def test_get_player_via_id_player1_random_id(self):
        with self.assertRaises(ValueError):
            player = self.game.get_player_via_id(100)

    # Player 2 - ID für Player 2 - Richtig
    def test_get_player_via_id_player2_right_id(self):
        player = self.game.get_player_via_id(99)
        self.assertEqual(self.p2, player)

    # Player 2 - ID für Player 1 - Falsch
    def test_get_player_via_id_player2_wrong_id(self):
        player = self.game.get_player_via_id(33)
        self.assertNotEqual(self.p2, player)

    # Player 2 - random ID  - Falsch
    def test_get_player_via_id_player2_random_id(self):
        player = self.game.get_player_via_id(888)
        self.assertNotEqual(self.p2, player)

if __name__ == '__main__':
    unittest.main()
