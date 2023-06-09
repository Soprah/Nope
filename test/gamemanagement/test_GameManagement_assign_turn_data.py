import unittest
from unittest.mock import MagicMock

from src.gamemanagement.GameManagement import GameManagement


class TestGameManagementAssignTurnData(unittest.TestCase):
    def setUp(self):
        self.gm = GameManagement.get_instance(self=GameManagement)
        self.gm.rooms = {}
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
        self.turn_data = {
            "token": 24,
            "selected_cards": [94, 26, 47],
        }

    def tearDown(self):
        self.gm.rooms = {}


    def test_assign_turn_data_game_exists_right_player(self):
        # Ignoriert für diesen Testfall die Funktion der DataConvert Klasse
        dc_mock = MagicMock()
        dc_mock.net_to_gamelogic.return_value = None

        # Room mit zwei Spieler bauen
        self.gm.set_room(self.p1_data)
        self.gm.set_room(self.p2_data)

        self.assertIsNone(self.gm.assign_turn_data(self.turn_data))

        # Assertion methode:
        # Prüft, ob die Funktion, die wir ignorieren wollen,
        # ... auch tatsächlich ignoriert wird
        dc_mock.net_to_gamelogic.assert_not_called()


if __name__ == '__main__':
    unittest.main()
