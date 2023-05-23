from src.gamelogic.card.Card import Card


class NumberCard(Card):
    def __init__(self, id: object, color: object, number: object) -> object:
        super().__init__(id, color)
        if number not in (1, 2, 3):
            raise ValueError("The number must be 1, 2 or 3")
        self.number = number

    def __str__(self):
        return super().__str__() + f" Number: {self.number}"