from src.gamelogic.card.ActionCard import ActionCard
from src.gamelogic.card.JokerCard import JokerCard
from src.gamelogic.card.NumberCard import NumberCard
from src.gamelogic.card.RestartCard import RestartCard
from src.gamelogic.card.SelectionCard import SelectionCard
from src.gamelogic.card.TheoreticalCard import TheoreticalCard


class ViewCard(ActionCard):

    allowed_colors = (("red"), ("blue"), ("yellow"), ("green"))
    def __init__(self, id, color):
        if color not in self.allowed_colors:
            raise ValueError("Ungültige Farbe !")
        super().__init__(id, color)
        self.theoretical_card = None

    def __repr__(self):
        if self.theoretical_card is None:
            return super().__str__() + f" Effect: View Previous_Number: None Previous_Color: None"
        else:
            return super().__str__() + f" Previous_Number: {self.get_number()} Previous_Color: {self.get_color()}"

    def __str__(self):
        if self.theoretical_card is None:
            return super().__str__() + f" Effect: View Previous_Number: None Previous_Color: None"
        else:
            return super().__str__() + f" Previous_Number: {self.get_number()} Previous_Color: {self.get_color()}"

    def set_theoretical_card(self, card_underneath):
        """
        Copies the necessary values of card_underneath to the theoretical card reference

        :param card_underneath: the card underneath the ViewCard
        """
        if isinstance(card_underneath, (NumberCard, JokerCard)):
            number = card_underneath.get_number()
            color = card_underneath.get_color()
        elif isinstance(card_underneath, RestartCard):
            dict_values = card_underneath.to_dict_top_card()
            number = dict_values.get("content")
            color = dict_values.get("color")
        elif isinstance(card_underneath, SelectionCard):
            number = card_underneath.get_number()
            color = card_underneath.get_color()
        else:
            number = 1
            color = card_underneath.color
        if self.theoretical_card is None:
            self.theoretical_card = TheoreticalCard(number, color)
        else:
            raise ValueError("A theoretical card has already been set.")

    def clear_theoretical_card(self):
        """
        Clears the reference to the theoretical card
        """
        self.theoretical_card = None

    def get_number(self):
        if self.theoretical_card is not None:
            return self.theoretical_card.number
        else:
            return 1

    def get_color(self):
        if self.theoretical_card is not None and self.theoretical_card.color is not None:
            return self.theoretical_card.color
        else:
            return self.color

    def to_dict_top_card(self):
        """
        Creates a dictionary with the 'theoretical' attributes when the given card is a top_card

        local_color: Default value if the game starts
        local_number: Default value if the game starts
        :return: dict
        """

        local_color = self.get_color()
        local_number = self.get_number()
        return {
            "id": self.id,
            "color_amount": len(local_color),
            "color": local_color,
            "type": "number",
            "content": local_number
        }

    def to_dict_actual_card(self):
        """
        Creates a dictionary with the 'actual' card attributes when the given card is not a top_card

        :return: dict
        """
        return {
            "id": self.id,
            "color_amount": len(self.color),
            "color": self.color,
            "type": "action",
            "content": "view"
        }
