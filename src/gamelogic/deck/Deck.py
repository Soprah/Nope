from src.gamelogic.card.Card import Card
from src.gamelogic.card.NumberCard import NumberCard

import random

class Deck:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.cards = []
        self.draw_stack = []
        self.discard_stack = []
        self.build()

    def build(self):
        id_count = 1

        n = [1, 2, 3]
        f1 = [("red"), ("blue"), ("green"), ("yellow")]
        f2 = [("red", "blue"), ("red", "green"), ("red", "yellow"), ("blue", "green"), ("blue", "yellow"),
              ("green", "yellow")]

        #Einfarbige Karten: 20 Stück
        for number in n:
            for farbe in f1:
                if number == 3:
                    self.cards.append(NumberCard(1, farbe, id_count, number))
                    id_count = id_count + 1
                else:
                    for i in range(2):
                        self.cards.append(NumberCard(1, farbe, id_count, number))
                        id_count = id_count + 1

        # Zweifarbige Karten: 66 Stück
        for i in range(2):
            for farbe in f2:
                # 24Karten für Zahl 1
                self.cards.append(NumberCard(2, (farbe[0], farbe[1]), id_count, 1))
                id_count = id_count + 1
                self.cards.append(NumberCard(2, (farbe[1], farbe[0]), id_count, 1))
                id_count = id_count + 1
                # 24Karten für Zahl 2
                self.cards.append(NumberCard(2, (farbe[0], farbe[1]), id_count, 2))
                id_count = id_count + 1
                self.cards.append(NumberCard(2, (farbe[1], farbe[0]), id_count, 2))
                id_count = id_count + 1
        for farbe in f2:
            # 18 Karten für Zahl 3
            self.cards.append(NumberCard(2, (farbe[0], farbe[1]), id_count, 3))
            id_count = id_count + 1
            self.cards.append(NumberCard(2, (farbe[1], farbe[0]), id_count, 3))
            id_count = id_count + 1
            self.cards.append(NumberCard(2, (farbe[0], farbe[1]), id_count, 3))
            id_count = id_count + 1

        # self.shuffle()
        self.draw_stack = self.cards.copy()

    def draw_card(self):
        return self.draw_stack.pop()

    def discard_card(self, card):
        if not isinstance(card, Card):
            raise TypeError("The discarded item must be a card!")
        elif card not in self.cards:
            raise ValueError("The discarded card does not exist in the deck!")
        else:
            self.discard_stack.append(card)
        return card

