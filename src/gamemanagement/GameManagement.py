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

	rooms = {}
	sessions = {}

	def receive_player_data(self, player_data):
		self.set_room(player_data)

	def set_room(self, player_data):
		"""
		Baut einen neuen Room oder weist Spieler einen bestehenden Raum zu

		:param player_data: Dictionary der Spielerdaten (token, name, room)
		"""
		room_id = player_data.get("room")
		player_id = player_data.get("token")
		player_name = player_data.get("name")
		# Room existiert
		if self.does_room_exist(room_id):
			room = self.get_room(room_id)
			player_1 = room.get("player_1")
			player_2 = Player(player_name, player_id)
			game = Game(player_1, player_2)
			self.add_game_to_sessions(game, player_1.id, player_2)
			room["game"] = game
			room["player_2"] = player_2
		# Room existiert nicht
		else:
			player = Player(player_name, player_id)
			self.rooms[room_id] = {
				"game": None,
				"player_1": player,
				"player_2": None
			}

	def get_room(self, room_id):
		return self.rooms[room_id]

	def does_room_exist(self, room_id):
		return self.get_room(room_id) is not None

	def get_game(self, p_id):
		game = self.sessions.get(p_id)
		return game

	def add_game_to_sessions(self, game, p1_id, p2_id):
		self.sessions[p1_id] = game
		self.sessions[p2_id] = game

	# TODO: Startet das Spiel
	def start_game(self):
		pass

	# TODO: Verschickt die Spielzugdaten, welches von DataConvert bereitgestellt wurde
	def send_turn_data(self):
		pass

	# TODO: Empfängt die Spielzugdaten, welches von Network geliefert wird
	def receive_turn_data(self):
		pass