import uuid

class Player:

    def __init__(self, deck, name):
        self.id = uuid.uuid4()
        self.name = name
        self.deck = deck
        self.hand = []

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
