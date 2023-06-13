from flask import flask, render_template, jsonify
from flask_socketio import SocketIO, emit
from AIPlayer import aiPlayer, test

artificialPlayer = aiPlayer()
test()

socketio = SocketIO()


# Client tritt Server bei und gibt einen Roomcode an
@socketio.on("connect")
def handle_connect(roomcode):
    print("Connected to server")
    emit('join_game', artificialPlayer.username, roomcode)


# Username des Gegners wird gezeigt
@socketio.on("game_start")
def game_start(data):
    print("Client started the game")
    opponent_name = {
        "opponent_username": data["opponent_username"]
    }
    print("Username of the opponent: " + opponent_name["opponent_username"])


# Spielstand wird vom Server Empfangen
@socketio.on("next_turn")
def next_turn(data):
    turn_data = {
        "previous_selected_cards": data["previous_selected_cards"],
        "top_card": data["top_card"],
        "amount_opponent_hand": data["amount_opponent_hand"],
        "own_hand_cards": data["own_hand_cards"]
    }
    if "previous_selected_cards" not in turn_data.values():
        raise Exception("Turn Data empty, server has send unusable data")
    # TODO: Methode für KI schreiben, die den Zug berechnet
    artificialPlayer.think_of_move(turn_data)


# Spielzug wird an den Server geschickt
@socketio.on("select_cards")
def select_cards(cards):
    print("Turn data send")
    emit('play_cards', jsonify(cards))


# Resultat des Spiels wird gezeigt
@socketio.on("game_end")
def game_end(data):
    print("Game has ended")
    game_result = {
        "game_end": data["game_end"]
    }
    print("Result of the game: " + game_result["game_end"])


@socketio.on("request_history_list")
def request_history_list():
    emit('get_history_list')


@socketio.on("receive_history_list")
def receive_history_list(history_list):
    artificialPlayer.select_game_history(history_list)


@socketio.on("request_history")
def request_history(history_id):
    # TODO: Methode für artificialPlayer schreiben um history auszuwählen
    emit('get_history', history_id)


@socketio.on("receive_history")
def receive_history(data):
    # TODO: History einlesen und ausgeben
    print(data)


roomcode = input("Bitte Raumcode eingeben")

socketio.connect()