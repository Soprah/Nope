from flask import request
from flask_socketio import emit
from flask_socketio import SocketIO

socketio = SocketIO()

users = {}


@socketio.on("connect")
def handle_connect():
    print("Client connected!")


@socketio.on("user_join")
def handle_user_join(username):
    if username in users:
        return False
    print(f"User {username} joined!")
    users[username] = request.sid
    print(users)


@socketio.on("new_message")
def handle_new_message(message):
    print(f"New message: {message}")
    username = None
    for user in users:
        if users[user] != request.sid:
            username = user
    print(request.sid)
    print(username)
    emit("chat", {"message": message, "username": username}, room=users[username])


@socketio.on("disconnect")
def handle_disconnect():
    print("Client disconnected!")
    username = None
    for user in users:
        if users[user] == request.sid:
            username = user
    if username:
        del users[username]


@socketio.on("next_turn")
def handle_next_turn(user, turn_data):
    print(f"Next turn: {user} {turn_data}")
    emit("next_turn", turn_data, room=users[user])
