from flask import request, jsonify
from flask_socketio import emit, SocketIO

socketio = SocketIO()

users = {}


@socketio.on("connect")
def handle_connect():
    print("Client connected!")


@socketio.on("join_game")
def handle_join_game(username, roomcode):
    if username in users:
        return False
    print(f"User {username} joined!")
    users[username] = request.sid
    print(users)
    player_data = {
        "username": username,
        "token": request.sid,
        "roomcode": roomcode
    }
    # TODO: gm.add_player(player_data)


@socketio.on("game_start")
def handle_game_start(user, opponent):
    print("Game started")
    emit("game_start", opponent, room=users[user])


@socketio.on("next_turn")
def handle_next_turn(user, turn_data):
    print(f"Next turn: {user} {turn_data}")
    emit("next_turn", turn_data, room=users[user])


@socketio.on("play_cards")
def handle_selected_cards(data):
    # TODO: Fehler abfangen
    turn = {
        "selected_cards": data["selected_cards"],
        "token": request.sid
    }
    print(f"Received selected cards: {turn}")
    # TODO: gm.receive_data(turn)


@socketio.on("game_end")
def handle_game_end(user, result):
    print("game ended")
    emit("game_end", result, room=users[user])


@socketio.on("disconnect")
def handle_disconnect():
    print("Client disconnected!")
    username = None
    for user in users:
        if users[user] == request.sid:
            username = user
    if username:
        del users[username]


@socketio.on("get_history_list")
def handle_get_games_list():
    print("get history list")
    history_list = {}  # TODO: gm.get_history_list()
    emit("receive_history_list", jsonify(history_list), room=request.sid)


@socketio.on("get_history")
def handle_get_history(hist_id):
    print("get history")
    history = {}  # TODO: gm.get_history(hist_id)
    emit("receive_history", jsonify(history), room=request.sid)
