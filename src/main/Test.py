from src.gamelogic.game.Game import Game
from src.gamelogic.player.client_simulation.ClientSimulation import ClientSimulation
from src.gamelogic.turn.Turn import Turn

# l = []
# l.append(1)
# l.append(2)
# l.append(3)
# d = {"previous_selected_cards": l}
# print(d.get("previous_selected_cards")[-1])

"""
game = Game("Eric", "Marc")
first_turn = Turn(game.active_player, game.deck.discard_stack[-1])
sent_turn_data = game.send_turn_data(first_turn)
for card in sent_turn_data.get("own_hand_cards"):
    print(f"Spielerkarte: {card}")
client = ClientSimulation()
client.top_card = sent_turn_data.get("previous_selected_cards")
print("Top Karte: ", client.top_card)
client.player_hand = sent_turn_data.get("own_hand_cards")
# for card in client.player_hand:
#     print(f"Spielerkarte: {card}")
client.possible_moves = client.create_dict_possible_moves()
for key in client.possible_moves.keys():
    for card in client.possible_moves.get(key):
        print(f"Mögliche Karte: {key} - {card}")
client_picked_cards = client.execute_lazy(client.possible_moves, client.top_card.number)
for card in client_picked_cards:
    print(f"Ausgewählte Karte: {card}")
client_picked_cards_ids = [card.id for card in client_picked_cards]
for id in client_picked_cards_ids:
    print(f"ID einer ausgewählten Karte: {id}")
client_sends_data = {"id": client_picked_cards_ids}
checked_list = game.receive_turn_data(client_sends_data)
print("Länge der gecheckten Liste: ", len(checked_list))
for item in checked_list:
    print(item)
print("Ist der Zug gültig? ", first_turn.is_valid(checked_list))
"""

# """
game = Game("Eric", "Marc")
first_turn = Turn(game.active_player, game.deck.discard_stack[-1])
sent_turn_data = game.send_turn_data(first_turn)
for card in sent_turn_data.get("own_hand_cards"):
    print(f"Spielerkarte: {card}")
print("********")
print("Top Karte:   ",sent_turn_data.get("previous_selected_cards"))
print("********")
client = ClientSimulation()

# client_picked_cards = client.select_valid_cards(sent_turn_data)
# print("Anzahl der möglichen Farben: ", len(client.possible_moves))
# for key in client.possible_moves.keys():
#     for card in client.possible_moves.get(key):
#         print(f"Mögliche Karte: {key} - {card}")
# for card in client_picked_cards:
#     print("Ausgewählte Karte: ", card)

client_processed_data = game.active_player.CS_select_cards(sent_turn_data)
print("Das Dictionary vom Client: ", client_processed_data)
if len(client_processed_data.get("selected_cards")) != 0:
    for card in client_processed_data.get("selected_cards"):
        print("Ausgewählte Karte/ID: ", card)
checked_list = game.receive_turn_data(client_processed_data)
print("Länge der gecheckten Liste: ", len(checked_list))
for item in checked_list:
    print(item)
print("Ist der Zug gültig? ", first_turn.is_valid(checked_list))