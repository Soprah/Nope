import unittest


class TestGameManagementSetRoom(unittest.TestCase):
    def setUp(self):
        self.player_1_name = "Rainer"
        self.player_2_name = "Sabine"



# Fehlerquellen
    # Spieler ist schon Teil des Room
    # Spieler ist schon Teil eines laufenden Spiels
    # Der Room ist voll

if __name__ == '__main__':
    unittest.main()
