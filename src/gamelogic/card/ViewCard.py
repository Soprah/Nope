from src.gamelogic.card.ActionCard import ActionCard


class ViewCard(ActionCard):

    allowed_colors = (("red"), ("blue"), ("yellow"), ("green"))
    def __init__(self, id, color):
        if color not in self.allowed_colors:
            raise ValueError("Ungültige Farbe !")
        super().__init__(id, color)

    def __str__(self):
        return super().__str__() + f" Effect: View"