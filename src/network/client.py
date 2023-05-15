import requests
from flask import json

authentication_id = -1
name = 'Tim'
artificialinteligent = -1

def connect():
	url = "http://127.0.0.1:5000/connect"
	req = requests.get(url=url)
	if(req.ok):
		global authentication_id
		authentication_id = req.json()['authentication_id']

#Eine Netzwerkfunktion, damit der Spieler vom Spiel eine ID bekommt.
def add_player_to_game():
	url = "http://127.0.0.1:5000/add_player_to_game"
	global authentication_id
	global name
	data = json.dumps({'authentication_id': authentication_id, 'name': name})
	req = requests.post(url=url, json=data)
	if(req.ok):
		print(req.text)

#Test
print("test connect")
connect()
print(authentication_id)
print("tets add_player_to_game")
add_player_to_game()
