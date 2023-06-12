import unittest

from src.gamemanagement.GameManagement import GameManagement


class TestGameManagementIsPlayerInRoom(unittest.TestCase):
    def setUp(self):
        self.gm = GameManagement.get_instance(self=GameManagement)
        self.p1_data = {
            "room": "r1",
            "token": 24,
            "name": "rainer"
        }
        self.p2_data = {
            "room": "r1",
            "token": 61,
            "name": "sabine"
        }

    def test_is_player_in_room_false(self):
        # Room bauen
        self.gm.set_room(self.p1_data)
        # Prüfen, ob der Spieler im Room ist
        r_id = self.p2_data.get("room")
        p_id = self.p2_data.get("token")
        self.assertFalse(self.gm.is_player_in_room(r_id, p_id))

    def test_is_player_in_room_true(self):
        # Room bauen
        self.gm.set_room(self.p1_data)
        # Prüfen, ob der Spieler im Room ist
        r_id = self.p1_data.get("room")
        p_id = self.p1_data.get("token")
        self.assertTrue(self.gm.is_player_in_room(r_id, p_id))

if __name__ == '__main__':
    unittest.main()
