from src.gamelogic.game.Game import Game
from src.gamelogic.game.GameState import FinishTurnState
from src.gamelogic.player.Player import Player


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
        """
		Schnittstelle zwischen Netzwerk und GameManagement, wenn sich ein Spieler verbindet

		:param player_data: name, token, room
		:return:
		"""
        return self.set_room(player_data)

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

    def receive_turn_data(self, turn_data):
        """
		Schnittstelle zwischen Netzwerk und GameManagement, wenn die Spielzugdaten gesendet werden

		:param turn_data: Spielzugdaten des Clients
		"""
        is_valid = self.assign_turn_data(turn_data)
        p_id = turn_data.get("token")
        game = self.get_game(p_id)
        # Lässt die Karten ablegen. Returnt nichts
        if is_valid and isinstance(game.get_state(), FinishTurnState):
            game.execute()
        return is_valid

    def assign_turn_data(self, turn_data):
        p_id = turn_data.get("token")
        game = self.get_game(p_id)
        if game is not None:
            if game.active_player.id == p_id:
                is_valid = game.execute(turn_data)
                return is_valid
            else:
                print(f"Der Spieler mit der ID {p_id} war nicht am Zug !")
                return False
        else:
            print(f"Es gibt kein laufendes Spiel mit der Spieler ID {p_id} !")
            return False

    def get_turn_data(self, game):
        turn_data = game.execute()
        user = game.active_player.name
        turn_data_player = {
            "turn_data": turn_data,
            "user": user
        }
        return turn_data_player

    def start_game_p1_data(self, game):
        p1_dict = {
            "user": game.player_1.name,
            "opponent": game.player_2.name
        }
        return p1_dict

    def start_game_p2_data(self, game):
        p2_dict = {
            "user": game.player_2.name,
            "opponent": game.player_1.name
        }
        return p2_dict

    def start_game(self, game):
        return self.get_turn_data(game)

    """
	def start_game(self, game):
		turn_data = game.execute()
		user = game.active_player.name
		turn_data_player = {
			"turn_data": turn_data,
			"user": user
		}
		return turn_data_player
	"""

    def send_turn_data(self, data, active_player):
        to_send_data = {
            "turn_data": data,
            "user": active_player
        }
    # events.handle_next_turn(to_send_data)
