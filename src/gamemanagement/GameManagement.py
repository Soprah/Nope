from src.gamelogic.player.Player import Player
from src.gamelogic.game.Game import Game

class GameManagement:

	"""
    HINWEIS:    Diese Klasse verwaltet alle Spielsitzungen

                Grundsätzlicher Ablauf:
                ⇾ GM bekommt Daten
                	* session_id
                	* Funktion (Request), die ausgeführt werden soll
                ⇾ GM sucht passendes Spiel für die empfangenen Daten.
                ⇾ GM weist die empfangenen Daten der gesuchten Spielsitzung zu
    """

	def __init__(self):
		self.game_sessions = {}

	def assign_player_to_game(self, p1_id, p1_name, p2_id, p2_name):
		p1 = Player(p1_name, p1_id)
		p2 = Player(p2_name, p2_id)
		game = Game(p1, p2)
		self.game_sessions[p1_id] = game
		self.game_sessions[p2_id] = game

gm = GameManagement()
gm.assign_player_to_game(11, "p1 ", 22, "p2")
print(gm.game_sessions.get(11))
print(gm.game_sessions.get(22))
gm.assign_player_to_game(33, "p3", 44, "p4")
print(gm.game_sessions.get(33))
print(gm.game_sessions.get(44))

