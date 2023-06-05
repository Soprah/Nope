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

    # TODO | Spezialfall: Zweite Karte, die gelegt wird, ist eine ViewCard
    #   * Bisher:
    #       * Bei dem Fall, wo eine SelectionCard keinen theoretical_card Verweis besitzt,
    #       * ... werden default werte bei "to_dict_actual_card()" zurückgegeben
    #           * local_number = 1
    #   * Problem:
    #       *  Wenn die Methode, die die letzte Karte unter der ViewCard zurückgibt, die
    #       * ... Selection Card zurückgibt, die beim Spielstart als erstes auf dem
    #       * ... Ablagestapel lag, weiß die Funktion nicht, welche Werte sie von der
    #       * ... Selection Card nehmen soll, da der theoretical Card Verweis 'None' ist.
    #   * Lösung 1:
    #       * Diesen Spezialfall in der jeweiligen Methode hard coden
    #       => redundanter Code
    #   * Lösung 2:
    #       * Selection Card anders gestalten
    #       * Sie besitzt immer default-werte
    #       => Macht aber keinen Sinn, oder?
    #   * Lösung 3:
    #       * eine Methode bauen, die "get_theoretical_card_values" heißt
    #       * Wenn die Selection Card TC-Werte hat, gibt er die zurück
    #       * Ansonsten: Die festgelegten Werte
    #           * Bei einer single color: number=1
    #           * Bei einer four color: number=1, color= die 4 farben
    #       * Vorteil dieser Lösung:
    #       * Das kann man sowohl in "to_dict_top_card()", als auch bei dem ViewCard-Fall, nutzen
    #       => Macht am meisten Sinn !!!

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