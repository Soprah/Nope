from src.gamelogic.card.Card import Card
from src.gamelogic.card.JokerCard import JokerCard
from src.gamelogic.card.NumberCard import NumberCard
from src.gamelogic.card.RestartCard import RestartCard
from src.gamelogic.card.SelectionCard import SelectionCard
from src.gamelogic.card.ViewCard import ViewCard
from src.gamelogic.game.Game import Game


class DataConvert:

    # TODO / WIP
    def gamelogic_to_net(self, game):
        previous_selected_cards = self.to_dict_previous_selected_cards(game)
        top_card = self.to_dict_top_card(game)
        amount_opponent_hand = self.to_dict_amount_opponent_hand(game)
        own_hand_cards = self.to_dict_own_hand_cards(game)
        turn_data = {
            "previous_selected_cards": previous_selected_cards,
            "top_card": top_card,
            "amount_opponent_hand": amount_opponent_hand,
            "own_hand_cards": own_hand_cards,
        }
        return turn_data

    def to_dict_previous_selected_cards(self, game):
        data = []
        if self.is_game_start(game):
            return data
        else:
            previous_turn = game.turns[-2]
            for card in previous_turn.selected_cards:
                if isinstance(card, (ViewCard, SelectionCard, RestartCard)):
                    data.append(card.to_dict_actual_card())
                else:
                    data.append(card.to_dict())
            return data

    # TODO
    def to_dict_top_card(self, game):
        current_turn = game.turns[-1]
        top_card = current_turn.top_card
        if isinstance(top_card, (ViewCard, SelectionCard, RestartCard)):
            data = top_card.to_dict_top_card()
        else:
            data = top_card.to_dict()
        return data

    # TODO
    def to_dict_amount_opponent_hand(self, game):
        data = {}
        return data

    # TODO
    def to_dict_own_hand_cards(self, game):
        data = {}
        return data

    # TODO
    #   * Wann setze ich den theoretical_card wert der ViewCard?
    def was_only_viewcard_played(self, game):
        pass


    '''
    def gamelogic_to_net(self, game):
        turn_data = {}
        current_turn = game.turns[-1]
        if len(game.turns) == 1:
            opponent = game.player_2
            if isinstance(current_turn.top_card, (SelectionCard, ViewCard)):
                top_card_dict = current_turn.top_card.to_dict_top_card()
            else:
                top_card_dict = current_turn.top_card.to_dict()
            turn_data = {
                "previous_selected_cards": [],
                "top_card": top_card_dict,
                "amount_opponent_cards": len(opponent.hand),
                "own_hand_cards": current_turn.player.hand
            }
        # elif len(self.turns) > 1:
        #     previous_turn = game.turns[-2]
        #     turn_data = {
        #         "previous_selected_cards": previous_turn.selected_cards,
        #         "top_card": previous_turn.top_card,
        #         "amount_opponent_cards": len(previous_turn.player.hand),
        #         "own_hand_cards": current_turn.player.hand
        #     }
        return turn_data
    '''

    def is_game_start(self, game):
        return len(game.turns) == 1

    def net_to_gamelogic(self, input_dict, game):
        """
        Prüft KartenIDs / Zusatzdaten

        :param game: Das Spiel, welches die Daten bekommt
        :param input_dict: Vom Client erstellte Dictionary
            "token": player id
            "selected_cards": card ids
            ggf. Wahlwerte bei SelectionCard:
                "chosen_number": zahl
                "chosen_color": farbe
        :return: Dictionary inklusive der entsprechenden Karten, die tatsächlich existieren
        """
        # Welcher Spieler schickt die Data
        player = game.get_player_via_id(input_dict.get("token"))
        # IDs der Karten
        selected_cards = input_dict.get("selected_cards")
        built_cards = []
        # Nicht-finale Version des Dicts, was returnt wird
        output_dict = {
            "token": input_dict.get("token"),
            "game": game,
            "selected_cards": selected_cards
        }

        if self.is_empty(selected_cards):
            return output_dict

        if not self.are_all_integers(selected_cards):
            game.disqualify_player(player, "Es dürfen nur Zahlen als IDs übergeben werden")
            return output_dict

        if self.are_duplicate_ids(selected_cards):
            game.disqualify_player(player, "Die IDs enthalten Duplikate")
            return output_dict

        else:
            # ID in Spielerhand
            if self.is_list_in_player_hand(selected_cards, game):

                # Baut Kartenobjekte
                built_cards = self.build_card_objects(selected_cards, game)
                input_dict["selected_cards"] = built_cards

                # Nur SelectionCard
                if self.is_only_selection_card(input_dict.get("selected_cards")):
                    # TODO | Keine variable speichert das ergebnis folgender funktion:
                    s_dict = self.execute_steps_for_selection_card(input_dict, game)
                    return s_dict

            # ID nicht in Spielerhand
            else:
                # Spieler wegen falscher ID disqualifizieren
                game.disqualify_player(player, "ID existiert nicht in der Spielerhand")

        output_dict["selected_cards"] = built_cards
        return output_dict

    def execute_steps_for_selection_card(self, modified_input_dict, game):
        """
        Führt notwendige Checks und Zuweisungen für eine einzeln gelegte SelectionCard aus

        :param modified_input_dict: Besteht aus
            "selected_cards": Liste aus gebauten Kartenobjekten
        :param game: Spielobjekt
        """
        selected_cards = modified_input_dict.get("selected_cards")
        player_id = modified_input_dict.get("token")
        player = game.get_player_via_id(player_id)
        selection_card = selected_cards[0]
        modified_input_dict["game"] = game

        allowed_colors = (("red",), ("blue",), ("green",), ("yellow",))
        allowed_numbers = [1, 2, 3]

        # Einfarbig
        if len(selection_card.color) == 1:
            # Dict besitzt Wahlwert
            if "chosen_number" in modified_input_dict:
                # Richtige Zahl
                if modified_input_dict.get("chosen_number") in allowed_numbers:
                    # Theoretical Card setzen
                    number = modified_input_dict.get("chosen_number")
                    selection_card.set_theoretical_card(number)
                    modified_input_dict.__delitem__("chosen_number")
                else:
                    # Spieler wegen falschen Wahlwerten disqualifizieren
                    game.disqualify_player(player,
                                           "Es wurden falsche Wahlwerte für die einfarbige SelectionCard übergeben")
            # Dict besitzt nicht Wahlwert
            else:
                game.disqualify_player(player, "Der Schlüssel 'chosen_number' befand sich nicht im dictionary")

        # Vierfarbig
        elif len(selection_card.color) == 4:
            # Dict besitzt Wahlwerte
            if "chosen_number" in modified_input_dict and "chosen_color" in modified_input_dict:
                if modified_input_dict.get("chosen_number") in allowed_numbers and modified_input_dict.get(
                        "chosen_color") in allowed_colors:
                    # Theoretical Card setzen
                    number = modified_input_dict.get("chosen_number")
                    color = modified_input_dict.get("chosen_color")
                    selection_card.set_theoretical_card(number, color)
                    modified_input_dict.__delitem__("chosen_number")
                    modified_input_dict.__delitem__("chosen_color")
                else:
                    # Spieler wegen falschen Wahlwerten disqualifizieren
                    game.disqualify_player(player,
                                           "Es wurden falsche Wahlwerte für die vierfarbige SelectionCard übergeben")
            # Dict besitzt nicht Wahlwerte
            else:
                game.disqualify_player(player,
                                       "Einer oder beide Schlüssel 'chosen_number', 'chosen_color' befanden sich nicht im dictionary")
        return modified_input_dict

    def are_all_integers(self, cards):
        return not any(not isinstance(x, int) for x in cards)

    def is_empty(self, cards):
        return len(cards) == 0

    def is_list_in_player_hand(self, list, game):
        for id in list:
            c = game.deck.cards_dict.get(id)
            if c not in game.active_player.hand:
                return False
        return True

    def build_card_objects(self, list, game):
        cards = []
        for id in list:
            c = game.deck.cards_dict.get(id)
            cards.append(c)
        return cards

    def are_duplicate_ids(self, list_of_ids):
        return len(list_of_ids) != len(set(list_of_ids))

    def is_only_selection_card(self, list):
        return len(list) == 1 and isinstance(list[0], SelectionCard)
