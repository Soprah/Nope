from src.gamelogic.card.Card import Card
from src.gamelogic.deck.Deck import Deck
from src.gamelogic.game.Game import Game
from src.gamelogic.player.Player import Player
from src.gamelogic.turn.Turn import Turn


deck = Deck()
for c in deck.cards:
    print(c)

print(len(deck.cards))

game = Game("eric", "marc")
print(game.deck.discard_stack[-1])
