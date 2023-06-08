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

	# TODO: Empfängt Spielerdaten (name=string, token=string, room=string) und weist Spieler einem Raum zu
	def receive_player_data(self, player_data):
		self.set_room(player_data)


	# TODO: Baut einen neuen room mit der id oder ergänzt spieler zu bestehenden room
	def set_room(self, player_data):
		room_id = player_data.get("room")
		player_id = player_data.get("token")
		player_name = player_data.get("name")
		player = Player(player_name, player_id)
		if self.does_room_exist(room_id):
			self.rooms[room_id] = {
				"game": None,
				"player_2": player,
				"player_2": None
			}
		elif self.does_room_need_just_one_player(room_id):
			self.rooms[room_id] = {


			}

	def get_room(self, room_id):
		return self.rooms[room_id]

	def does_room_exist(self, room_id):
		return self.get_room(room_id) is not None

	def does_room_need_just_one_player(self, room_id):
		room = self.get_room(room_id)
		return room["player_1"] is not None and room["player_2"] is None

	# TODO: Startet das Spiel
	def start_game(self):
		pass

	# TODO: Verschickt die Spielzugdaten, welches von DataConvert bereitgestellt wurde
	def send_turn_data(self):
		pass

	# TODO: Empfängt die Spielzugdaten, welches von Network geliefert wird
	def receive_turn_data(self):
		pass