import uuid

from src.gamelogic.player.client_simulation.ClientSimulation import ClientSimulation
from src.Datenbank.connector import DatabaseConnector

class Player:

    def __init__(self, name, authentication_id):
        self.id = authentication_id
        self.name = name
        self.deck = None
        self.hand = []
        self.is_disqualified = False
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
            #DatabaseConnector(host, port, database, user, password).execute_query("QUERY")
            return discarded_card
        else:
            raise ValueError("Card not in player's hand.")

    def CS_select_cards(self, dict_turn_data):
        cards = self.client_simulation.select_valid_cards(dict_turn_data)
        cards_id = []
        if len(cards) != 0:
            for card in cards:
                cards_id.append(card.id)
        player_turn_data = {"selected_cards": cards_id, "token": self.id}
        return player_turn_data

    def __str__(self):
        return f"Spieler ID: {self.id}, Spieler Name: {self.name}"

    def __repr__(self):
        return f"Spieler ID: {self.id}, Spieler Name: {self.name}"