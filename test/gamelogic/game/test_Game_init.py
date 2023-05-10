import unittest

from src.gamelogic.game.Game import Game


class TestGameInit(unittest.TestCase):


    def setUp(self):
        self.player_1_name = "Eric"
        self.player_2_name = "Marc"

    def test_correct_init(self):
        game = Game(self.player_1_name, self.player_2_name)
        self.assertEqual(len(game.turns), 0)
        self.assertEqual(len(game.deck.draw_stack), 69)
        self.assertEqual(len(game.deck.discard_stack), 1)
        self.assertEqual(game.player_1.name, self.player_1_name)
        self.assertEqual(game.player_2.name, self.player_2_name)
        self.assertEqual(game.active_player.name, self.player_1_name)
        self.assertEqual(len(game.player_1.hand), 8)
        # self.assertEqual(len(game.active_player), 8)
        self.assertEqual(len(game.player_2.hand), 8)





if __name__ == '__main__':
    unittest.main()
