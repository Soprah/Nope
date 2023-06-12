from src.gamelogic.card.ActionCard import ActionCard
from src.gamelogic.card.Card import Card
from src.gamelogic.card.JokerCard import JokerCard
from src.gamelogic.card.NumberCard import NumberCard
from src.gamelogic.card.RestartCard import RestartCard
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
        # (key=color, value=cards) Dictionary. Mögliche, valide Züge
        self.possible_moves = {}
        # Anzahl der Versuche einen Spielzug auszuführen
        self.turn_attempt = 1
        # Gibt an, ob der vom Spieler gemachte Spielzug gültig ist
        self.is_turn_valid = None

    def get_cards_matching_color(self):
        """
        Spielerhandkarten werden nach Farbe der top_card sortiert

        :return: dict
        """
        dict = {}
        c = self.top_card.get_color()
        for i in range(len(c)):
            required_color = c[i]
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
        return len(cards) >= self.top_card.get_number()

    def create_dict_possible_moves(self):
        """
        Überprüft, ob es für eine/mehr Farben genügend Karten in der Spielerhand
            für einen validen Zug gibt

        :return: dictionary der möglichen Farben
        """
        self.possible_moves = self.get_cards_matching_color()
        keys_to_remove = []
        for key in self.possible_moves.keys():
            if not self.has_sufficient_matching_cards(key):
                keys_to_remove.append(key)
        for key in keys_to_remove:
            self.possible_moves.pop(key)
        return self.possible_moves

    def is_color_consistent(self, color, selected_cards):
        """
        Überprüft, ob eine Farbe in jeder Karte der Liste vorhanden ist

        :param color: Farbe, die gesucht / verglichen wird
        :param selected_cards: Liste an Karten, die mit Farbe durchsucht wird
        :return: boolean
        """
        flag = True
        for card in selected_cards:
            if color not in card.get_color():
                flag = False
        return flag

    def is_valid(self, selected_cards):
        c = selected_cards
        self.turn_attempt = self.turn_attempt + 1
        self.selected_cards = c
        self.possible_moves = self.create_dict_possible_moves()

        if self.player_has_set():
            self.is_turn_valid = self.selected_cards_represent_set(c) or self.played_valid_action_card(c)
        else:
            self.is_turn_valid = len(c) == 0 or self.played_valid_action_card(c)
        return self.is_turn_valid

    def has_common_color(self, new_card):
        set_new_card = set(new_card.color)
        set_top_card = set(self.top_card.color)
        common_color = (set_new_card & set_top_card)
        return len(common_color) > 0

    def played_valid_action_card(self, cards):
        if len(cards) == 0:
            return False
        card = cards[0]
        return len(cards) == 1 and isinstance(card, ActionCard) and self.has_common_color(card)

    def is_another_attempt_necessary(self):
        """
        Überprüft, ob ein Spieler noch einen Spielzug ausführen darf/muss

        :return: boolean
        """
        return len(self.selected_cards) == 0 and self.turn_attempt == 2 and self.is_turn_valid

    def player_has_set(self):
        return len(self.possible_moves) != 0

    def selected_cards_represent_set(self, selected_cards):
        flag = []
        for color in self.possible_moves.keys():
            color_and_len_flag = self.is_color_consistent(color, selected_cards) and len(
                selected_cards) == self.top_card.get_number()
            flag.append(color_and_len_flag)
        return True in flag