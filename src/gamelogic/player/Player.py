import uuid

from src.gamelogic.player.client_simulation.ClientSimulation import ClientSimulation


class Player:

    def __init__(self, deck, name):
        self.id = uuid.uuid4()
        self.name = name
        self.deck = deck
        self.hand = []
        self.is_disqualified = False
        ''' Client Simulation Attribute: '''
        # Placeholder
        self.client_simulation = ClientSimulation()

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

    def CS_select_cards(self, dict_turn_data):
        cards = self.client_simulation.select_valid_cards(dict_turn_data)
        cards_id = []
        if len(cards) != 0:
            for card in cards:
                cards_id.append(card.id)
        player_turn_data = {"selected_cards": cards_id, "token": self.id}
        return player_turn_data