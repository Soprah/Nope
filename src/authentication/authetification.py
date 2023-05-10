from flask import jsonify
import random
import time

sessions = {}
session_timeout = 1000

#for development
def test_draw_card(session_id):
    return jsonify({'card' : 'b2'})

def test_make_move(session_id, move):
    return 1
################

def connect():
    session_id = int(random.random()*(10**16))
    global sessions
    global session_timeout
    sessions[session_id] = time.time() + session_timeout
    return jsonify({'session_id' : session_id})

def verify(session_id):
    global sessions
    if session_id in sessions:
        if (time.time() < sessions[session_id]):
            return True
    return False

def draw_card(data):
    session_id = data['session']
    if (verify(session_id)):   
        res = test_draw_card(session_id)
        return res
    return -1

def make_move(data):
    session_id = data['session']
    if (verify(session_id)):
        move = data['move']
        res = test_make_move(session_id, move)
        return res
    return -1

            
    
