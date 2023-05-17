from flask import Flask, request
import src.authentification.authetification as au

app = Flask(__name__)

@app.route('/connect', methods=['GET'])
def connect():
	return au.connect()

@app.route('/add_player_to_game', methods=['POST'])
def add_player_to_game():
	data = request.get_json()
	return au.add_player_to_game(data)
