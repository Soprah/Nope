import uuid

class Player:

    def __init__(self, deck, name):
        self.id = uuid.uuid4()
        self.name = name
        self.deck = deck
        self.hand = []
