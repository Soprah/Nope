import uuid

from src.gamelogic.player.client_simulation.ClientSimulation import ClientSimulation


class Player:

    def __init__(self, name, authentication_id):
        self.id = authentication_id
        self.name = name
        self.deck = None
        self.hand = []
        self.is_disqualified = False
        self.game_result = None
        ''' Client Simulation Attribute: '''
        self.client_simulation = ClientSimulation()

    def get_id(self):
        return self.id

    def set_deck(self, deck):
        self.deck = deck

    def draw_card(self):
        drawn_card = self.deck.draw_card()
        self.hand.append(drawn_card)
        return drawn_card

    def discard_card(self, card):
        if card in self.hand:
            discarded_card = self.hand.pop(self.hand.index(card))
            self.deck.discard_stack.append(discarded_card)
            return discarded_card
        else:
            raise ValueError("Card not in player's hand.")

    def __str__(self):
        return f"Spieler ID: {self.id}, Spieler Name: {self.name}"

    def __repr__(self):
        return f"Spieler ID: {self.id}, Spieler Name: {self.name}"