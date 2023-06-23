import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, '..', '..')
sys.path.append(src_dir)

from flask import Flask, request
from flask_socketio import emit, SocketIO
import json
from src.gamemanagement.GameManagement import GameManagement
import src.database.DatabaseManagement as DBM

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

gm = GameManagement.get_instance(self=GameManagement)
users = {}


@socketio.on("connect")
def handle_connect():
    print("Client connected!")


@socketio.on("join_game")
def handle_join_game(join_data):
    # Client in "users" speichern
    join_data = json.loads(join_data)
    username = join_data["name"]
    if username in users:
        return False
    print(f"User {username} joined!")
    users[username] = request.sid

    # Baut Paket für GameManagement
    player_data = {
        "name": username,
        "token": request.sid,
        "room": join_data["room"]
    }

    # GameManagement reagiert auf das Paket
    message = gm.receive_player_data(player_data)
    print(message)

    # Room enthält jetzt 2 Spieler
    if message == "Successfully assigned a player to an existing room !":
        # Verschickt den Namen des Gegners
        p_id = player_data.get("token")
        game = gm.get_game(p_id)
        p1_data = gm.start_game_p1_data(game)
        p2_data = gm.start_game_p2_data(game)
        handle_game_start(p1_data)
        handle_game_start(p2_data)

        # Spiel starten - Turn Data verschicken
        turn_data = gm.start_game(game)
        handle_next_turn(turn_data)


def handle_game_start(start_data):
    user = start_data["user"]
    start_data = {
        "opponent_username": start_data["opponent"],
    }
    print("*** *** GAME START *** ***")
    emit("game_start", json.dumps(start_data), room=users[user])


def handle_next_turn(next_turn):
    user = next_turn["user"]
    turn_data = next_turn["turn_data"]
    # print(f"Next turn: {user} {turn_data}")
    emit("next_turn", json.dumps(turn_data), room=users[user])


@socketio.on("play_cards")
def handle_selected_cards(data):
    data = json.loads(data)
    turn = {
        "selected_cards": data["selected_cards"],
        "token": request.sid
    }
    is_turn_valid = gm.receive_turn_data(turn)
    p_id = turn.get("token")
    game = gm.get_game(p_id)
    if not is_turn_valid or game.is_game_over():
        # TODO: Hier die History aus der Datenbank mittels Datenbank API holen !
        history = "Hallo Welt"
        p1_game_end_dict = {
            "result": game.player_1.game_result,
            "user": game.player_1.name,
            "history": history
        }
        p2_game_end_dict = {
            "result": game.player_2.game_result,
            "user": game.player_2.name,
            "history": history
        }
        # Event game end
        handle_game_end(p1_game_end_dict)
        handle_game_end(p2_game_end_dict)
    else:
        turn_data = gm.get_turn_data(game)
        handle_next_turn(turn_data)



def handle_game_end(end_data):
    print("*** CLASS: Events ***")
    user = end_data["user"]
    result = {
        "result": end_data["result"],
        # TODO: History hier angeben oder nachher durch Datenbank ?
        "history": end_data["history"]
    }
    print("game ended")
    emit("game_end", json.dumps(result), room=users[user])


@socketio.on("disconnect")
def handle_disconnect():
    username = None
    for user in users:
        if users[user] == request.sid:
            username = user
            print(f"Client {username} disconnected!")
    if username:
        del users[username]


if __name__ == '__main__':
    socketio.run(app, allow_unsafe_werkzeug=True)
