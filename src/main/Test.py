from src.gamelogic.card.NumberCard import NumberCard
from src.gamelogic.card.SelectionCard import SelectionCard
from src.gamelogic.card.ViewCard import ViewCard
from src.gamelogic.game.Game import Game
from src.gamelogic.player.Player import Player
from src.dataconvert.DataConvert import DataConvert
from src.gamelogic.turn.Turn import Turn
from src.gamemanagement.GameManagement import GameManagement

p1 = Player("Eric", "33")
p2 = Player("Marc", "19")
game = Game(p1, p2)
# for c in game.deck.cards:
#     print(c)

print(game.get_state())
game.execute()
print(game.state_output)
game.change_state()

print(game.get_state())
game.execute()
print(game.state_output)
game.change_state()