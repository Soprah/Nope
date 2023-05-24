from src.gamelogic.card.NumberCard import NumberCard


class JokerCard(NumberCard):

    def __init__(self, id):
        super().__init__(id, (("red"), ("blue"), ("yellow"), ("green")), 1)

    def __str__(self):
        return super().__str__() + f" Typ: Joker"
