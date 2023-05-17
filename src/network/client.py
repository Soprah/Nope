import requests
from src.gamelogic.player.Player import Player

myPlayer = Player("TestPlayer", -1)

def connect():
	url = "http://127.0.0.1:5000/connect"
	req = requests.get(url=url)
	if(req.ok):
		global myPlayer
		session_id = req.json()['session_id']
		myPlayer.set_id(session_id)

#Eine Netzwerkfunktion, damit der Spieler vom Spiel eine ID bekommt.
def add_player_to_game():
	url = "http://127.0.0.1:5000/add_player_to_game"
	global myPlayer
	req = requests.post(url=url, json={'session_id' : myPlayer.get_id()})
	if(req.ok):
		pass#TODO

#Test
print("test connect")
print(draw_card())
connect()
print(myPlayer)
print("tets draw_card")
print(draw_card())
