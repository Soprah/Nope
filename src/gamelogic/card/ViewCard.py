from src.gamelogic.card.ActionCard import ActionCard
from src.gamelogic.card.TheoreticalCard import TheoreticalCard


class ViewCard(ActionCard):

    allowed_colors = (("red"), ("blue"), ("yellow"), ("green"))
    def __init__(self, id, color):
        if color not in self.allowed_colors:
            raise ValueError("Ungültige Farbe !")
        super().__init__(id, color)
        self.theoretical_card = None

    def __str__(self):
        return super().__str__() + f" Effect: View"

    # TODO "Was muss der Verweis 'theoretical_card' speziell bei einer ViewCard speichern?"
    #   * Immer: number, color
    #   * Gibt es eine Fallunterscheidung zwischen 'actual_card' und 'top_card' ?

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