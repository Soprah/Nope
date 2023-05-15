import unittest

from src.gamelogic.game.Game import Game
from src.gamelogic.player.Player import Player


class GameNextTurn(unittest.TestCase):

    def setUp(self):
        self.p1 = Player("Eric", 3)
        self.p2 = Player("Marc", 19)
        self.game = Game(self.p1, self.p2)

    def test_next_turn_game_start(self):
        first_turn = self.game.next_turn()

        # Spieler 1 = Turn Spieler = Aktiver Game Spieler
        self.assertTrue(first_turn.player == self.game.player_1 == self.game.active_player)
        # Oberste Karte vom Spieldeck = Turn Top Karte
        self.assertEqual(first_turn.top_card, self.game.deck.discard_stack[-1])
        # Länge der turn-liste vom Spiel wurde um 1 erhöht
        self.assertEqual(len(self.game.turns), 1)

    def test_next_turn_mid_game(self):
        first_turn = self.game.next_turn()
        second_turn = self.game.next_turn()

        # Spieler 2 = Turn Spieler = Aktiver Game Spieler
        self.assertTrue(second_turn.player == self.game.player_2 == self.game.active_player)
        # Oberste Karte vom Spieldeck = Turn Top Karte
        self.assertEqual(second_turn.top_card, self.game.deck.discard_stack[-1])
        # Länge der turn-liste vom Spiel wurde um 1 erhöht
        self.assertEqual(len(self.game.turns), 2)



if __name__ == '__main__':
    unittest.main()
