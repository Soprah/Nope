from src.gamelogic.card.Card import Card


class ActionCard(Card):

    def __init__(self, id, color, effect):
        super().__init__(id, color)
        if effect not in ["RESTART", "VIEW", "SELECTION"]:
            raise ValueError("Ungültiger Effekt für Aktionskarte!")
        self.effect = effect

    def __str__(self):
        return super().__str__() + f" Effect: {self.effect}"