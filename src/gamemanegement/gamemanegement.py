from src.gamelogic.player.Player import Player
from src.gamelogic.game.Game import Game

game_sessions = {}
waiting_player_session_id = -1

def add_player_to_game(session_id, name):
	global waiting_player_session_id
    if(waiting_player_session_id > 0):
	    player1 = Player()
	    player2 = Player()
	    pass