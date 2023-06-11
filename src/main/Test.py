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
output = dc.gamelogic_to_net(game)

hand = output.get("own_hand_cards")
for i in range(8):
    print("Soll:", game.active_player.hand[i])
    print("Tatsächlich:", hand[i])

amount = output.get("amount_opponent_hand")
print(amount)

actual_top_card = output.get("top_card")
expected_top_card = game.turns[-1].top_card
print("Soll top: ", expected_top_card)
print("Tatsächlich top: ", actual_top_card)

p = output.get("previous_selected_cards")
print(p)