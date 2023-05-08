import unittest

from src.gamelogic.game.Game import Game


class TestGameReceiveTurnData(unittest.TestCase):

    def setUp(self):
        self.game = Game("eric", "marc")

    """ Prüft, ob die empfangenen Karten, die der Spieler abwerfen möchte, gültig sind"""
    def test_receive_turn_data(self):
        pass


if __name__ == '__main__':
    unittest.main()
