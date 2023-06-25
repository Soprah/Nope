import psycopg2

connection = None
cursor = None

def connect():   
    try:
        print('Connecting to the PostgreSQL database...')
        global connection
        connection = psycopg2.connect(host="172.18.0.3", database="nope", user="postgres", password="postgres")
        global cursor
        cursor = connection.cursor()
        print('PostgreSQL database version:')
        cursor.execute('SELECT version()')
        db_version = cursor.fetchone()
        print(db_version)
        return True
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return False

def game_to_database(game):
    """ Methode zum Schreiben des Game Objekts in die Datenbank"""
    game_id = game.id
    turn_number = 0
    for turn in game.turns:
        player_name = turn.player
        top_card_id = turn.top_card['id']
        selected_cards = turn.selected_cards
        selected_card_ids = ""
        first = True
        for card in selected_cards:
            if first:
                selected_card_ids = card['id']
                first = False
            else:
                selected_card_ids += ", {}".format(card['id'])
        is_turn_valid = turn.is_turn_valid
        insert_turns_into_database(game_id, turn_number, player_name, top_card_id, selected_card_ids, is_turn_valid)
        turn_number += 1

def insert_turns_into_database(game_id, turn_number, player_name, top_card, selected_cards, is_turn_valid):
    global cursor
    command = """INSERT INTO turns (game_id, turn_number, player_name, top_card, selected_cards, is_turn_valid) VALUES (%s,%s,%s,%s,%s,%s);"""
    cursor.execute(command, (game_id, turn_number, player_name, top_card, selected_cards, is_turn_valid))
    global connection
    connection.commit()

def get_history(game_id):
    command = """SELECT turn_number, player_name, top_card, selected_cards, is_turn_valid FROM turns WHERE game_id = %s;"""
    global cursor
    cursor.execute(command, (game_id,))
    history = cursor.fetchall()
    global connection
    connection.commit()
    print(history)
    return history

def get_game_ids_in_database():
    command = """SELECT DISTINCT game_id FROM turns;"""
    global cursor
    cursor.execute(command)
    game_ids = cursor.fetchall()
    global connection
    connection.commit()
    print(game_ids)
    return game_ids

def insert_match_into_database(winner_name, loser_name, reason):
    global cursor
    if reason is not None:
        command = """INSERT INTO matches (winner_name, loser_name, reason) VALUES (%s,%s,%s);"""
        cursor.execute(command, (winner_name, loser_name, reason))
    else:
        command = """INSERT INTO matches (winner_name, loser_name) VALUES (%s,%s);"""
        cursor.execute(command, (winner_name, loser_name))
    global connection
    connection.commit()

def get_win_amount_of_user(winner_name):
    command = """SELECT COUNT(*) FROM matches WHERE winner_name = %s;"""
    global cursor
    cursor.execute(command, (winner_name,))
    matches = cursor.fetchall()
    global connection
    connection.commit()
    print(matches)

def disconnect():
    global connecttion
    if connection is not None:
        connection.close()
        print('Database connection closed.')
    global cursor
    if cursor is not None:
        cursor.close()