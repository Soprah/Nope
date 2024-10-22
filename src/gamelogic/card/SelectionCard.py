from src.gamelogic.card.ActionCard import ActionCard
from src.gamelogic.card.TheoreticalCard import TheoreticalCard


class SelectionCard(ActionCard):

    def __init__(self, id, color):
        super().__init__(id, color)
        self.theoretical_card = None

    def __repr__(self):
        if self.theoretical_card is None:
            return super().__str__() + f" Effect: Selection Chosen_Number: None Chosen_Color: None"
        else:
            return super().__str__() + f" Chosen_number: {self.get_number()} Chosen_color: {self.get_color()}"

    def __str__(self):
        if self.theoretical_card is None:
            return super().__str__() + f" Effect: Selection Chosen_Number: None Chosen_Color: None"
        else:
            return super().__str__() + f" Chosen_number: {self.get_number()} Chosen_color: {self.get_color()}"

    def set_theoretical_card(self, number, color=None):
        """
        Saves the choice of the client within a theoretical card

        :param number: choice of the client for a single color selection card
        :param color: choice of the client for a four color selection card
        """
        if self.theoretical_card is None:
            client_choice = TheoreticalCard(number, color)
            self.theoretical_card = client_choice
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
            "content": "selection"
        }