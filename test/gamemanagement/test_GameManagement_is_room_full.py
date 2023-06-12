import unittest

from src.gamemanagement.GameManagement import GameManagement


class TestGameManagementIsRoomFull(unittest.TestCase):
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

    def test_is_room_full_false(self):
        # Room bauen
        self.gm.set_room(self.p1_data)
        # Prüfen, ob der room voll ist
        id = self.p1_data.get("room")
        self.assertFalse(self.gm.is_room_full(id))

    def test_is_room_full_true(self):
        # Room bauen
        self.gm.set_room(self.p1_data)
        # Room füllen
        self.gm.set_room(self.p2_data)
        # Prüfen, ob der room voll ist
        id = self.p1_data.get("room")
        self.assertTrue(self.gm.is_room_full(id))


if __name__ == '__main__':
    unittest.main()