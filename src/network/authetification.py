from flask import Response, jsonify, json
import uuid
import time
import src.gamemanagement.GameManagement as gm

sessions = {}
session_timeout = 1000


def connect():
    player_authentication_id = uuid.uuid4().__str__()
    global sessions
    global session_timeout
    sessions[player_authentication_id] = time.time() + session_timeout
    return jsonify({'authentication_id' : player_authentication_id})


def verify(player_authentication_id):
    global sessions
    if player_authentication_id in sessions:
        if time.time() < sessions[player_authentication_id]:
            return True
    return False


def add_player_to_game(data):
    player_data = json.loads(data)
    player_authentication_id = player_data['authentication_id']
    if verify(player_authentication_id):
        return gm.assign_player_to_game(player_authentication_id, player_data['name'])
    else:
        return Response("not valide authentication id", status=404)
        

            
    
