from src.gamelogic.card.NumberCard import NumberCard


class JokerCard(NumberCard):

    allowed_colors = (("red"), ("blue"), ("yellow"), ("green"))
    def __init__(self, id, color):
        if color != self.allowed_colors:
            raise ValueError("Ungültige Farbkombination!")
        super().__init__(id, color, 1)

    def __str__(self):
        return super().__str__() + f" Typ: Joker"
