from src.gamelogic.card.SelectionCard import SelectionCard
from src.gamelogic.card.ViewCard import ViewCard
from src.gamelogic.game.Game import Game
from src.gamelogic.player.Player import Player
from src.dataconvert.DataConvert import DataConvert

dc = DataConvert()
p1 = Player("Eric", 33)
p2 = Player("Marc", 19)
game = Game(p1, p2)
# for c in game.deck.cards:
#     print(c)

game.next_turn()
p1_dict = dc.get_amount_opponent_hand(game)
p2_dict = dc.get_amount_opponent_hand(game)
print(p1_dict)
print(p2_dict)
# n_card = game.deck.cards_dict.get(9)
# v_card = game.deck.cards_dict.get(92)
#
# expected_out_hard = {
#     "id": -1,
#     "color_amount": 1,
#     "color": ("red",),
#     "type": "number",
#     "content": 1
# }
# first_turn_dict = {
#     "token": p1.id,
#     "selected_cards": [v_card.id]
# }
#
# # Erster Spielzug Simulation
# p1.hand = [v_card]
# game.deck.discard_stack[0] = n_card
# first_turn = game.next_turn()
# first_turn.top_card = n_card
# print("First Card:",first_turn.top_card)
#
# # Zweiter Spielzug Simulation
# second_turn = game.next_turn()
# game.switch_active_player()
# print("Die zu legende ViewCard: ", p1.hand[0])
# processed_dict = dc.net_to_gamelogic(first_turn_dict, game)
# print(processed_dict)
# processed_view_card = processed_dict.get("selected_cards")[0]
# second_turn.top_card = processed_view_card
# print(processed_view_card)
