from src.gamelogic.card.Card import Card
from src.gamelogic.card.JokerCard import JokerCard
from src.gamelogic.card.NumberCard import NumberCard

import random

from src.gamelogic.card.RestartCard import RestartCard
from src.gamelogic.card.SelectionCard import SelectionCard
from src.gamelogic.card.ViewCard import ViewCard


class Deck:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.cards_dict = {}
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

    # Zahlenkarten

        # Einfarbige Karten: 20 Stück
        for number in n:
            for farbe in f1:
                if number == 3:
                    self.cards.append(NumberCard(id_count, farbe, number))
                    id_count = id_count + 1
                else:
                    for i in range(2):
                        self.cards.append(NumberCard(id_count, farbe, number))
                        id_count = id_count + 1

        # Zweifarbige Karten: 66 Stück
        for i in range(2):
            for farbe in f2:
                # 24Karten für Zahl 1
                self.cards.append(NumberCard(id_count, (farbe[0], farbe[1]), 1))
                id_count = id_count + 1
                self.cards.append(NumberCard(id_count, (farbe[1], farbe[0]), 1))
                id_count = id_count + 1
                # 24Karten für Zahl 2
                self.cards.append(NumberCard(id_count, (farbe[0], farbe[1]), 2))
                id_count = id_count + 1
                self.cards.append(NumberCard(id_count, (farbe[1], farbe[0]), 2))
                id_count = id_count + 1
        for farbe in f2:
            # 18 Karten für Zahl 3
            self.cards.append(NumberCard(id_count, (farbe[0], farbe[1]), 3))
            id_count = id_count + 1
            self.cards.append(NumberCard(id_count, (farbe[1], farbe[0]), 3))
            id_count = id_count + 1
            self.cards.append(NumberCard(id_count, (farbe[0], farbe[1]), 3))
            id_count = id_count + 1

    # Aktionskarten

        # Neustart / Restart: 4 Stück
        for i in range(4):
            self.cards.append(RestartCard(id_count))
            id_count = id_count + 1

        # Durchblick / View: 4 Stück
        for color in f1:
            self.cards.append(ViewCard(id_count, color))
            id_count = id_count + 1

        # Auswahl / Selection: 6 Stück
        for color in f1:
            self.cards.append(SelectionCard(id_count, color))
            id_count = id_count + 1
        for i in range(2):
            self.cards.append(SelectionCard(id_count, (("red"), ("blue"), ("yellow"), ("green"))))
            id_count = id_count + 1

     # Jokerkarten

        for i in range(4):
            self.cards.append(JokerCard(id_count))
            id_count = id_count + 1

        self.cards_dict = self.create_dict_deck_copy(self.cards)
        # self.shuffle()
        self.draw_stack = self.cards.copy()


    def draw_card(self):
        if len(self.draw_stack) == 0:
            top_item = self.discard_stack.pop()
            self.draw_stack = self.discard_stack.copy()
            self.discard_stack.clear()
            self.discard_stack.append(top_item)
            random.shuffle(self.draw_stack)
        return self.draw_stack.pop()

    def discard_card(self, card):
        if not isinstance(card, Card):
            raise TypeError("The discarded item must be a card!")
        elif card not in self.cards:
            raise ValueError("The discarded card does not exist in the deck!")
        else:
            self.discard_stack.append(card)
        return card

    def initialize_discard_stack(self):
        first_card = self.draw_card()
        self.discard_stack.append(first_card)
        return first_card

    def shuffle(self):
        if len(self.cards) != 104:
            raise ValueError("The deck is not complete and therefore not ready to shuffle!")
        random.shuffle(self.cards)
        return self.cards

    def create_dict_deck_copy(self, card_list):
        deck_dict = {}
        for card in card_list:
            deck_dict[card.id] = card
        return deck_dict

    ''' NUR FÜR ENTWICKLUNGSZWECKE '''
    # Eine Methode, um bestimmte Karten für Testzwecke in der Hand des Spielers zu haben
        # draw_card_by_id(id)
            # Gibt mir eine bestimmte Karte