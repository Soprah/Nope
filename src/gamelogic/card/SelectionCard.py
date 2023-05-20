from src.gamelogic.card.ActionCard import ActionCard


class SelectionCard(ActionCard):

    def __init__(self, id, color):
        super().__init__(id, color)

    def __str__(self):
        return super().__str__() + f" Effect: Selection"