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
        client_choice = TheoreticalCard(number, color)
        self.theoretical_card = client_choice

    def clear_theoretical_card(self):
        """
        Clears the reference to the theoretical card
        """
        self.theoretical_card = None