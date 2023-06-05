from src.gamelogic.card.ActionCard import ActionCard


class RestartCard(ActionCard):

    def __init__(self, id):
        super().__init__(id, (("red"), ("blue"), ("yellow"), ("green")))

    def __str__(self):
        return super().__str__() + f" Effect: Restart"

    def to_dict_top_card(self):
        return {
            "id": self.id,
            "color_amount": len(self.color),
            "color": self.color,
            "type": "number",
            "content": 1
        }

    def to_dict_actual_card(self):
        return {
            "id": self.id,
            "color_amount": len(self.color),
            "color": self.color,
            "type": "action",
            "content": "restart"
        }