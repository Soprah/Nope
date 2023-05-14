from src.gamelogic.game.Game import Game
from src.gamelogic.player.client_simulation.ClientSimulation import ClientSimulation
from src.gamelogic.turn.Turn import Turn

# """
game = Game("Eric", "Marc")
first_turn = Turn(game.active_player, game.deck.discard_stack[-1])
sent_turn_data = game.send_turn_data(first_turn)
for card in sent_turn_data.get("own_hand_cards"):
    print(f"Spielerkarte: {card}")
print("********")
print("Top Karte:   ",sent_turn_data.get("previous_selected_cards"))
print("********")
client_processed_data = game.active_player.CS_select_cards(sent_turn_data)
print("Das Dictionary vom Client: ", client_processed_data)
if len(client_processed_data.get("selected_cards")) != 0:
    for card in client_processed_data.get("selected_cards"):
        print("Ausgewählte Karte/ID: ", card)
checked_list = game.receive_turn_data(client_processed_data)
print("Länge der gecheckten Liste: ", len(checked_list))
for item in checked_list:
    print(item)
turn_valid = first_turn.is_valid(checked_list)
another_attempt_necessary = first_turn.is_another_attempt_necessary()
print("Ist der Spielzug gültig?" ,turn_valid)
if turn_valid and another_attempt_necessary:
    print("Der Spieler konnte keine Karten legen und versucht es noch einmal")
    game.active_player.draw_card()
    game.active_player.draw_card()
    print("Der Spieler zieht zwei Karten:")
    for card in game.active_player.hand:
        print(f"Spielerkarte: {card}")
    second_sent_turn_data = game.send_turn_data(first_turn)
    second_client_processed_data = game.active_player.CS_select_cards(second_sent_turn_data)
    print("Der Spieler versucht es erneut")
    print("Das Dictionary vom Client: ", second_client_processed_data)
    if len(second_client_processed_data.get("selected_cards")) != 0:
        for card in second_client_processed_data.get("selected_cards"):
            print("Ausgewählte Karte/ID: ", card)
    second_checked_list = game.receive_turn_data(second_client_processed_data)
    print("Länge der gecheckten Liste: ", len(second_checked_list))
    for item in second_checked_list:
        print(item)
    second_turn_valid = first_turn.is_valid(second_checked_list)
    print("Ist der Spielzug gültig?", second_turn_valid)
# """

# game = Game("Eric", "Marc")
# game_sent_turn_data = game.send_turn_data(game.next_turn())
# for card in game_sent_turn_data.get("own_hand_cards"):
#     print(f"Spielerkarte: {card}")
# print("********")
# print("Top Karte:   ", game_sent_turn_data.get("previous_selected_cards"))
# print("********")
# client_processed_turn_data = game.active_player.CS_select_cards(game_sent_turn_data)
# game = Game("Eric", "Marc")
# game.run()