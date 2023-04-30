from src.gamelogic.card.Card import Card


class NumberCard(Card):
    def __init__(self, color_amount, color, id, number):
        super().__init__(color_amount, color, id)
        if number not in (1, 2, 3):
            raise ValueError("The number must be 1, 2 or 3")
        self.number = number