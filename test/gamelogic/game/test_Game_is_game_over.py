import unittest

from src.gamelogic.game.Game import Game
from src.gamelogic.player.Player import Player


class TestGameIsGameOver(unittest.TestCase):
    def setUp(self):
        self.p1 = Player("Eric", 3)
        self.p2 = Player("Marc", 19)
        self.game = Game(self.p1, self.p2)

    def test_is_game_over_p1_disqualified_True(self):
        self.game.player_1.is_disqualified = True
        is_over = self.game.is_game_over()
        self.assertTrue(is_over)

    def test_is_game_over_p2_disqualified_True(self):
        self.game.player_2.is_disqualified = True
        is_over = self.game.is_game_over()
        self.assertTrue(is_over)

    def test_is_game_over_p1_disqualified_False(self):
        is_over = self.game.is_game_over()
        self.assertFalse(is_over)

    def test_is_game_over_p2_disqualified_False(self):
        is_over = self.game.is_game_over()
        self.assertFalse(is_over)

    def test_is_game_over_p1_empty_hand_True(self):
        self.assertEqual(len(self.p1.hand), 8)
        self.assertIs(self.p1.deck, self.game.deck)
        self.assertIs(self.p1.deck, self.p2.deck)
        for c in self.game.player_1.hand.copy():
            self.game.player_1.discard_card(c)
        self.assertEqual(len(self.p1.hand), 0)
        is_over = self.game.is_game_over()
        self.assertTrue(is_over)

    def test_is_game_over_p2_empty_hand_True(self):
        self.assertEqual(len(self.p1.hand), 8)
        self.assertIs(self.p2.deck, self.game.deck)
        self.assertIs(self.p2.deck, self.p2.deck)
        for c in self.game.player_2.hand.copy():
            self.game.player_2.discard_card(c)
        self.assertEqual(len(self.p2.hand), 0)
        is_over = self.game.is_game_over()
        self.assertTrue(is_over)

    def test_is_game_over_p1_existing_hand_False(self):
        self.assertEqual(len(self.p1.hand), 8)
        is_over = self.game.is_game_over()
        self.assertFalse(is_over)

    def test_is_game_over_p2_existing_hand_False(self):
        self.assertEqual(len(self.p2.hand), 8)
        is_over = self.game.is_game_over()
        self.assertFalse(is_over)


if __name__ == '__main__':
    unittest.main()
