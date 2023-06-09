import unittest

from src.gamemanagement.GameManagement import GameManagement


class TestGameManagementSetRoom(unittest.TestCase):

    def setUp(self):
        self.gm = GameManagement.get_instance(self=GameManagement)
        self.gm.rooms = {}

    def tearDown(self):
        self.gm.rooms = {}

# Soll-Funktion

    # Raum leer ⇾ Erstelle Room mit Player
    def test_set_room_no_room_with_id(self):
        player_data = {
            "room": "r1",
            "token": 24,
            "name": "rainer"
        }

        s = self.gm.set_room(player_data)

        # richtige string ausgabe
        self.assertEqual("Successfully created a new room !", s)

        # 'rooms' besitzt nur einen room
        self.assertTrue(len(self.gm.rooms) == 1)

        # room besitzt richtige daten
        room = self.gm.get_room("r1")
        self.assertEqual(room.get("player_1").name, "rainer")
        self.assertIsNone(room.get("player_2"))
        self.assertIsNone(room.get("game"))

    # Raum halbvoll ⇾ Fülle Room mit Player
    def test_set_room_existing_room_with_id(self):
        player_1_data = {
            "room": "r1",
            "token": 24,
            "name": "rainer"
        }
        player_2_data = {
            "room": "r1",
            "token": 61,
            "name": "sabine"
        }
        self.gm.set_room(player_1_data)
        s = self.gm.set_room(player_2_data)

        # richtige string ausgabe
        self.assertEqual("Successfully assigned a player to an existing room !", s)

        # 'rooms' besitzt zwei rooms
        self.assertTrue(len(self.gm.rooms) == 1)

        # room besitzt richtige daten
        room = self.gm.get_room("r1")
        self.assertEqual(room.get("player_1").name, "rainer")
        self.assertEqual(room.get("player_2").name, "sabine")
        self.assertIsNotNone(room.get("game"))

        # game richtig in sessions gespeichert
        game_1 = self.gm.get_game(24)
        game_2 = self.gm.get_game(61)
        self.assertEqual(game_1, game_2)

# Fehlerquellen

    # Spieler ist schon Teil des Room
    def test_set_room_player_already_in_room(self):
        player_1_data = {
            "room": "r1",
            "token": 24,
            "name": "rainer"
        }
        self.gm.set_room(player_1_data)
        s = self.gm.set_room(player_1_data)

        player_id = player_1_data.get("token")
        room_id = player_1_data.get("room")
        self.assertFalse(self.gm.is_room_full(room_id))
        self.assertEqual(f"The player with the id {player_id} is already part of the desired room {room_id} !", s)

    # Der Room ist voll
    def test_set_room_room_is_already_full(self):
        player_1_data = {
            "room": "r1",
            "token": 24,
            "name": "rainer"
        }
        player_2_data = {
            "room": "r1",
            "token": 61,
            "name": "sabine"
        }
        player_3_data = {
            "room": "r1",
            "token": 8,
            "name": "christina"
        }

        self.gm.set_room(player_1_data)
        self.gm.set_room(player_2_data)
        s = self.gm.set_room(player_3_data)
        room_id = "r1"
        player_id = 8

        self.assertEqual(f"The room {room_id} is already full !", s)


if __name__ == '__main__':
    unittest.main()
