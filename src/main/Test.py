from src.gamelogic.card.NumberCard import NumberCard
from src.gamelogic.card.SelectionCard import SelectionCard
from src.gamelogic.card.ViewCard import ViewCard
from src.gamelogic.game.Game import Game
from src.gamelogic.player.Player import Player
from src.dataconvert.DataConvert import DataConvert
from src.gamelogic.turn.Turn import Turn

p1 = Player("Eric", 33)
p2 = Player("Marc", 19)
game = Game(p1, p2)
# for c in game.deck.cards:
#     print(c)

# Alle Karten des Nachziehstapels in den Ablagestapel kopieren
# Nachziehstapel leeren
# Oberste Karte des Ablagestapels zwischenspeichern zum Prüfen nachher