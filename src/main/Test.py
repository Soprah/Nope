from src.gamelogic.card.ViewCard import ViewCard
from src.gamelogic.game.Game import Game
from src.gamelogic.player.Player import Player

game = Game(Player("Eric", 3), Player("Marc", 19))
print("Karte vorher", game.deck.discard_stack[-1])
# game.deck.discard_stack[-1] = ViewCard(1, ("blue"))
new_turn = game.next_turn()
print(len(game.deck.discard_stack))
game_sent_turn_data = game.send_turn_data(new_turn)
for key in game_sent_turn_data.keys():
    print(f"Schlüssel: {key}, Wert: {game_sent_turn_data.get(key)}")