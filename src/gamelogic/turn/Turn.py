from src.gamelogic.card.Card import Card
from src.gamelogic.card.NumberCard import NumberCard
from src.gamelogic.player.Player import Player


class Turn:

    def __init__(self, player, top_card):
        if not isinstance(player, Player):
            raise TypeError(f"{player} is not from the Player class!")
        if not isinstance(top_card, Card):
            raise TypeError(f"{top_card} is not from the Card class!")
        self.player = player
        self.top_card = top_card
        self.selected_cards = []
        """ Hilfsattribute: """
        #
        self.possible_moves = {}

    # Man bekommt eine Liste von Karten, die der Spieler abwerfen MÖCHTE
    # is_valid() prüft, ob das zulässig ist
            # A: leere Liste
                    # Was: Schauen, ob tatsächlich kein Zug vom Spieler notwendig war
                    # Wie: Die Handkarten des Spielers mit der top_card vergleichen
                        # Wenn von einer Farbe genügend Karten gibt (genügend >= top_card.number), dann hätte es klappen können


    def get_cards_matching_color(self):
        """
        Spielerhandkarten werden nach Farbe der top_card sortiert

        :return: dict
        """
        dict = {}
        for i in range(len(self.top_card.color)):
            required_color = self.top_card.color[i]
            dict[required_color] = [card for card in self.player.hand
                                    if required_color in card.color]
        return dict

    def has_sufficient_matching_cards(self, color):
        """
        Überprüft, ob für eine Farbe genügend Karten vorhanden sind

        :param color: Eine Farbe der top_card
        :return: boolean
        """
        cards = self.possible_moves.get(color)
        if isinstance(self.top_card, NumberCard):
            if len(cards) >= self.top_card.number:
                return True
        return False

    def create_dict_possible_moves(self):
        """
        Überprüft, ob es für eine/mehr Farben genügend Karten in der Spielerhand
            für einen validen Zug gibt

        :return: dictionary der möglichen Farben
        """
        # Das Dictionary mit den ungecheckten Moves erstellt
        self.possible_moves = self.get_cards_matching_color()
        # Hier geht man mit der Hilfsfunktion, die eine Liste
        # ... für eine spezifische Farbe nach Validität prüft,
        # ... alle Listen nach Validität durch
        keys_to_remove = []
        for key in self.possible_moves.keys():
            if not self.has_sufficient_matching_cards(key):
                keys_to_remove.append(key)
        for key in keys_to_remove:
            self.possible_moves.pop(key)
        return self.possible_moves

    def is_valid(self, selected_cards):
        pass