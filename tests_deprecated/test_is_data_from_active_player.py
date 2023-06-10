import unittest

from src.gamelogic.game.Game import Game
from src.gamelogic.player.Player import Player
from src.gamelogic.dataconvert.DataConvert import DataConvert


class TestDataConvertIsDataFromActivePlayer(unittest.TestCase):

    def setUp(self):
        self.p1 = Player("Eric", 33)
        self.p2 = Player("Marc", 19)
        self.game = Game(self.p1, self.p2)
        self.dc = DataConvert()

    # Correct token
    def test_is_data_from_active_player_true(self):
        self.assertTrue(self.dc.is_data_from_active_player(33, self.game))


    # Incorrect token
    def test_is_data_from_active_player_false(self):
        self.assertFalse(self.dc.is_data_from_active_player(19, self.game))


if __name__ == '__main__':
    unittest.main()
