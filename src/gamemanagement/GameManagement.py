from src.gamelogic.player.Player import Player
from src.gamelogic.game.Game import Game
from src.gamemanagement.DataConvert import DataConvert


class GameManagement:

	"""
    HINWEIS:    Diese Klasse verwaltet alle Spielsitzungen

                Grundsätzlicher Ablauf:
                ⇾ GM bekommt Daten.
                ⇾ GM sucht passendes Spiel für die empfangenen Daten.
                ⇾ GM weist die empfangenen Daten der gesuchten Spielsitzung zu.
    """

	_instance = None

	def __init__(self):
		self.rooms = {}
		self.sessions = {}

	def get_instance(self):
		if GameManagement._instance is None:
			GameManagement._instance = GameManagement()
		return GameManagement._instance

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

		# # Abbruchbedingung 1
		if self.is_room_full(room_id):
			return f"The room {room_id} is already full !"
		# # Abbruchbedingung 2
		elif self.is_player_in_room(room_id, player_id):
			return f"The player with the id {player_id} is already part of the desired room {room_id} !"

		# Room existiert
		if self.does_room_exist(room_id):
			room = self.get_room(room_id)
			player_1 = room.get("player_1")
			player_2 = Player(player_name, player_id)
			game = Game(player_1, player_2)
			self.add_game_to_sessions(game, player_1.id, player_2.id)
			room["game"] = game
			room["player_2"] = player_2
			return "Successfully assigned a player to an existing room !"

		# Room existiert nicht
		else:
			player = Player(player_name, player_id)
			self.rooms[room_id] = {
				"game": None,
				"player_1": player,
				"player_2": None
			}
			return "Successfully created a new room !"

	def is_player_in_room(self, room_id, p_id):
		room = self.rooms.get(room_id)
		if room:
			p1 = room.get("player_1")
			p2 = room.get("player_2")
			return p1 and p1.id == p_id or p2 and p2.id == p_id
		return False

	def is_room_full(self, room_id):
		if room_id in self.rooms:
			room = self.rooms.get(room_id)
			p1 = room.get("player_1")
			p2 = room.get("player_2")
			return p1 and p2 is not None
		else:
			return False

	def get_room(self, room_id):
		return self.rooms[room_id]

	def does_room_exist(self, room_id):
		return room_id in self.rooms

	def get_game(self, p_id):
		game = self.sessions.get(p_id)
		return game

	def add_game_to_sessions(self, game, p1_id, p2_id):
		self.sessions[p1_id] = game
		self.sessions[p2_id] = game

	def assign_turn_data(self, turn_data):
		dc = DataConvert()
		p_id = turn_data.get("token")
		game = self.get_game(p_id)
		# Game existiert mit token
		if game is not None:
			# Richtiger Spieler?
			if game.active_player.id == p_id:
				# Daten übergeben
				dc.net_to_gamelogic(turn_data, game)
				return None
			# Nicht aktiver Spieler
			else:
				return f"Der Spieler mit der ID {p_id} war nicht am Zug !"
		# Kein Game existiert mit token
		else:
			return f"Es gibt kein laufendes Spiel mit der Spieler ID {p_id} !"



		# Abbruchbedingung - Kein laufendes Spiel mit token



	# TODO: Startet das Spiel
	def start_game(self):
		pass

	# TODO: Verschickt die Spielzugdaten, welches von DataConvert bereitgestellt wurde
	def send_turn_data(self):
		pass

	# TODO: Empfängt die Spielzugdaten, welches von Network geliefert wird
	def receive_turn_data(self):
		pass