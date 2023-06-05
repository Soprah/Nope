from src.gamelogic.card.Card import Card


class NumberCard(Card):
    def __init__(self, id, color, number):
        super().__init__(id, color)
        if number not in (1, 2, 3):
            raise ValueError("The number must be 1, 2 or 3")
        self.number = number

    def __str__(self):
        return super().__str__() + f" Number: {self.number}"

    def to_dict_top_card(self):
        return {
            "id": self.id,
            "color_amount": len(self.color),
            "colors": self.color,
            "type": "number",
            "content": self.number
        }

    def to_dict(self):
        return {
            "id": self.id,
            "color_amount": len(self.color),
            "color": self.color,
            "type": "number",
            "content": self.number
        }