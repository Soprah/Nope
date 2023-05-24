from src.gamelogic.card.ActionCard import ActionCard


class RestartCard(ActionCard):

    def __init__(self, id):
        super().__init__(id, (("red"), ("blue"), ("yellow"), ("green")))

    def __str__(self):
        return super().__str__() + f" Effect: Restart"