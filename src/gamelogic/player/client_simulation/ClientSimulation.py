import random

from src.gamelogic.card.Card import Card
from src.gamelogic.card.NumberCard import NumberCard


class ClientSimulation:

    """
    HINWEIS:    Diese Klasse simuliert einen Client

                ⇾ "ClientSimulation_Process"
                ⇾ Simuliert: Empfangen, Verarbeiten, Senden von turn_data
                ⇾ NUR für Entwicklungszwecke !
    """
    def __init__(self):
        self.top_card = None
        self.player_hand = []
        self.possible_moves = {}
        self.selected_cards = []

    def get_cards_matching_color(self):
        dict = {}
        for i in range(len(self.top_card.color)):
            required_color = self.top_card.color[i]
            dict[required_color] = [card for card in self.player_hand
                                    if required_color in card.color]
        return dict

    def has_sufficient_matching_cards(self, color):
        cards = self.possible_moves.get(color)
        if isinstance(self.top_card, NumberCard):
            if len(cards) >= self.top_card.number:
                return True
        return False

    def create_dict_possible_moves(self):
        self.possible_moves = self.get_cards_matching_color()
        keys_to_remove = []
        for key in self.possible_moves.keys():
            if not self.has_sufficient_matching_cards(key):
                keys_to_remove.append(key)
        for key in keys_to_remove:
            self.possible_moves.pop(key)
        return self.possible_moves

    def execute_lazy(self, card_pool, amount_cards):
        cards = []
        if isinstance(card_pool, dict):
            keys = list(card_pool.keys())
            # WICHTIGER Punkt:
            if len(keys) == 0:
                return cards
            ##################
            first_key = keys[0]
            for i in range(amount_cards):
                cards.append(card_pool[first_key].pop())
                if not card_pool[first_key]:
                    keys.remove(first_key)
        return cards

    def select_valid_cards(self, dict_turn_data):
        """
        Was ich brauche:
            ⇾ top_card des Ablagestapels (=number)
            ⇾ Dictionary mit möglichen Zügen (=possible_moves)

        :param dict_turn_data: Informationen über einen Spielzug als Dictionary
        :return: Liste an Karten, die der Spieler für einen Spielzug auswählt
        """
        self.top_card = dict_turn_data.get("previous_selected_cards")
        self.player_hand = dict_turn_data.get("own_hand_cards")
        self.create_dict_possible_moves()
        self.selected_cards = self.execute_lazy(self.possible_moves, self.top_card.number)
        return self.selected_cards