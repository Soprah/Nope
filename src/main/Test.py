from src.gamelogic.card.JokerCard import JokerCard
from src.gamelogic.deck.Deck import Deck

deck = Deck()
for card in deck.cards:
    print(card)

j = JokerCard(1, (("red"), ("blue"), ("yellow"), ("green")))
print(j)