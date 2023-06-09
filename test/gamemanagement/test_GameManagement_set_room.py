import unittest

from src.gamemanagement.GameManagement import GameManagement


class TestGameManagementSetRoom(unittest.TestCase):

    def setUp(self):
        self.gm = GameManagement.get_instance(self=GameManagement)

# Soll-Funktion

    # Raum leer ⇾ Erstelle Room mit Player
    def test_set_room_no_room_with_id(self):
        player_data = {
            "room": "r1",
            "token": 24,
            "name": "rainer"
        }

        self.gm.set_room(player_data)

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
        self.gm.set_room(player_2_data)

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
# Spieler ist schon Teil eines laufenden Spiels
# Der Room ist voll

if __name__ == '__main__':
    unittest.main()
