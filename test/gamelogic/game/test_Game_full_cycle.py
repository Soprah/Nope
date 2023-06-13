import unittest

from src.gamelogic.game.Game import Game
from src.gamelogic.game.GameState import NewTurnState
from src.gamelogic.player.Player import Player
from src.gamemanagement.GameManagement import GameManagement


class TestGameFullCycle(unittest.TestCase):
    def setUp(self):
        self.gm = GameManagement.get_instance(self=GameManagement)
        self.p1_join_data = {
            "room": "r1",
            "token": 24,
            "name": "rainer"
        }
        self.p2_join_data = {
            "room": "r1",
            "token": 61,
            "name": "sabine"
        }
    def tearDown(self):
        self.gm.rooms = {}

    def test_full_cycle(self):

        # ROOM ERSTELLEN
        self.gm.set_room(self.p1_join_data)
        self.gm.set_room(self.p2_join_data)
        self.assertTrue(len(self.gm.rooms) == 1)

        # Room besitzt richtige daten
        room = self.gm.get_room("r1")
        self.assertEqual(room.get("player_1").name, "rainer")
        self.assertEqual(room.get("player_2").name, "sabine")
        self.assertIsNotNone(room.get("game"))

        # Game richtig in sessions gespeichert
        game = self.gm.get_game(24)
        self.assertIsInstance(game, Game)
        self.assertEqual(self.gm.get_game(24), self.gm.get_game(61))

        # Game wartet auf Spielbeginn
        self.assertIsInstance(game.get_state(), NewTurnState)

        # GAME STARTEN
        turn_data = game.execute()

        # Paket richtig
        self.assertEqual(turn_data.get("top_card").get("id"), game.turns[-1].top_card.id)
        self.assertTrue(len(turn_data) == 4)
        hand_cards_ids = [
            turn_data.get("own_hand_cards")[0].get("id"),
            turn_data.get("own_hand_cards")[1].get("id"),
            turn_data.get("own_hand_cards")[2].get("id"),
            turn_data.get("own_hand_cards")[3].get("id"),
            turn_data.get("own_hand_cards")[4].get("id"),
            turn_data.get("own_hand_cards")[5].get("id"),
            turn_data.get("own_hand_cards")[6].get("id"),
            turn_data.get("own_hand_cards")[7].get("id"),
        ]
        for card in game.active_player.hand:
            self.assertIn(card.id, hand_cards_ids)
        self.assertTrue(turn_data.get("amount_opponent_hand") == len(game.player_2.hand))

if __name__ == '__main__':
    unittest.main()