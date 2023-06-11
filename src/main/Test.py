from src.gamelogic.card.SelectionCard import SelectionCard
from src.gamelogic.card.ViewCard import ViewCard
from src.gamelogic.game.Game import Game
from src.gamelogic.player.Player import Player
from src.dataconvert.DataConvert import DataConvert

# dc = DataConvert()
p1 = Player("Eric", 33)
p2 = Player("Marc", 19)
game = Game(p1, p2)
for c in game.deck.cards:
    print(c)

c1 = game.deck.cards_dict.get(71)
c2 = game.deck.cards_dict.get(80)
set_c1 = set(c1.color)
set_c2 = set(c2.color)

common = (set_c1 & set_c2)
t_common = tuple(common)
print(t_common)