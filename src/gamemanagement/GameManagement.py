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

		

	"""
	def __init__(self):
		self.game_sessions = {}
		self.game_

	def assign_player_to_game(self, p1_id, p1_name, p2_id, p2_name):
		if p1_id in self.game_sessions or p2_id in self.game_sessions or p1_id == p2_id:
			raise ValueError("Duplicate player ID!")

		p1 = Player(p1_name, p1_id)
		p2 = Player(p2_name, p2_id)
		game = Game(p1, p2)
		self.game_sessions[p1_id] = game
		self.game_sessions[p2_id] = game

	def get_game(self, p_id):
		game = self.game_sessions.get(p_id)
		return game
	"""

	# TODO: Empfängt Spielerdaten (name=string, token=string, room=string)
	def receive_player_data(self, player_data):
		pass

	# TODO: Sucht einen room mit der id
	def seek_room(self, room_id):
		pass

	# TODO: Baut einen room zum Spielen, wenn es einen room mit dem übergebenen string noch nicht gibt
	def build_room(self, room_id):
		pass

	# TODO: Startet das Spiel
	def start_game(self):
		pass

	# TODO: Verschickt die Spielzugdaten, welches von DataConvert bereitgestellt wurde
	def send_turn_data(self):
		pass

	# TODO: Empfängt die Spielzugdaten, welches von Network geliefert wird
	def receive_turn_data(self):
		pass