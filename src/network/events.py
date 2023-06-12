from flask import Flask, request, jsonify
from flask_socketio import emit, SocketIO
#from src.gamemanagement.GameManagement import GameManagement

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
#gm = GameManagement.get_instance(self=GameManagement)

users = {}


@socketio.on("connect")
def handle_connect():
    print("Client connected!")


@socketio.on("join_game")
def handle_join_game(join_data):
    username = join_data["name"]
    if username in users:
        return False
    print(f"User {username} joined!")
    users[username] = request.sid
    print(users)
    player_data = {
        "name": username,
        "token": request.sid,
        "room": join_data["room"]
    }
    #gm.receive_player_data(player_data)

def handle_game_start(start_data):
    user = start_data["user"]
    start_data = {
        "opponent_username": start_data["opponent"],
    }
    print("Game started")
    emit("game_start", jsonify(start_data), room=users[user])


def handle_next_turn(next_turn):
    user = next_turn["user"]
    turn_data = next_turn["turn_data"]
    print(f"Next turn: {user} {turn_data}")
    emit("next_turn", jsonify(turn_data), room=users[user])


@socketio.on("play_cards")
def handle_selected_cards(data):
    turn = {
        "selected_cards": data["selected_cards"],
        "token": request.sid
    }
    print(f"Received selected cards: {turn}")
    #gm.receive_turn_data(turn)


def handle_game_end(end_data):
    user = end_data["user"]
    result = {
        "result": end_data["result"],
        "history": end_data["history"]
    }
    print("game ended")
    emit("game_end", jsonify(result), room=users[user])


@socketio.on("disconnect")
def handle_disconnect():
    print("Client disconnected!")
    username = None
    for user in users:
        if users[user] == request.sid:
            username = user
    if username:
        del users[username]

if __name__ == '__main__':
    socketio.run(app)