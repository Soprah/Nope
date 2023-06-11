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

# color=red | number=2 | NUMBER
n_card = game.deck.cards_dict.get(9)
print("NUMBER:", n_card.get_color())
print("NUMBER:", n_card.get_number())
print()

# color=red,blue,yellow,green | number=1 | JOKER
j_card = game.deck.cards_dict.get(101)
print("JOKER:", j_card.get_color())
print("JOKER:", j_card.get_number())
print()

# color=red,blue,yellow,green | number=1 | RESTART
r_card = game.deck.cards_dict.get(87)
print("RESTART:", r_card.get_color())
print("RESTART:", r_card.get_number())
print()

# color=blue | number=None | VIEW
v_card = game.deck.cards_dict.get(92)
print("VIEW:", v_card.get_color())
print("VIEW:", v_card.get_number())
print()

# color=green | number=None | SINGLE SEL
ss_card = game.deck.cards_dict.get(97)
print("SINGLE SEL:", ss_card.get_color())
print("SINGLE SEL:", ss_card.get_number())
print()

# color=red,blue,yellow,green | number=None | color=None | MULTIPLE SEL
ms_card = game.deck.cards_dict.get(100)
print("MULTIPLE SEL:", ms_card.get_color())
print("MULTIPLE SEL:", ms_card.get_number())
print()