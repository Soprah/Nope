import json
# examples
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse
y = json.loads(x)

# controll
print(y["age"])

# Nope

def send_Info():
	# TODO ein int gibt an ob der Spieler oder gewonnen oder verloren hat oder
	return 0


def send_State():
	# TODO sendet Alle KArten + Oberste Karte im Ablagestapel + Anzahl der Karten des gegenspielers
	return 0


def send_History():
	# TODO sendet die gesammt Spiel History
	return 0


def send_Profile():
	# TODO sendet die Bestätigung zu einem Spiel mit der Angabe des Tokens
	return 0