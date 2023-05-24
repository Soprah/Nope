from flask import Flask, request
import network.authetification as au
from network import create_app, socketio

app = Flask(__name__)


@app.route('/connect', methods=['GET'])
def connect():
    return au.connect()


@app.route('/add_player_to_game', methods=['POST'])
def add_player_to_game():
    data = request.get_json()
    return au.add_player_to_game(data)


app = create_app()

socketio.run(app, allow_unsafe_werkzeug=True)
