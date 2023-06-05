from src.gamelogic.card.ActionCard import ActionCard
from src.gamelogic.card.TheoreticalCard import TheoreticalCard


class SelectionCard(ActionCard):

    def __init__(self, id, color):
        super().__init__(id, color)
        self.theoretical_card = None

    def __str__(self):
        return super().__str__() + f" Effect: Selection"

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

    def to_dict_top_card(self):
        """
        Creates a dictionary with the 'theoretical' attributes when the given card is a top_card

        :return: dict
        """
        local_color = self.color
        # TODO:
        #   * number = 1 is just a filler
        #   * Still need to think about the case when a selection card is the first top_card
        local_number = 1
        if self.theoretical_card is not None:
            local_number = self.theoretical_card.number
            if self.theoretical_card.color is not None:
                local_color = self.theoretical_card.color
        return {
            "id": -1,
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