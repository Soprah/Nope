import json
from flask import Flask, request

app = Flask(__name__)

# Request

@app.route("/login")
def login():
	name = request.args.get('name')
	send_Profile(name)

def send_Info():
	# TODO ein int gibt an ob der Spieler oder gewonnen oder verloren hat oder
	return 0


def send_State():
	# TODO sendet Alle KArten + Oberste Karte im Ablagestapel + Anzahl der Karten des gegenspielers
	return 0


def send_History():
	# TODO sendet die gesammt Spiel History
	return 0

# Respond

def send_Profile(name):
	# TODO sendet die Bestätigung zu einem Spiel mit der Angabe des Tokens
	return name + " id: 123456789"