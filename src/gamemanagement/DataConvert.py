from src.gamelogic.card.Card import Card
from src.gamelogic.card.JokerCard import JokerCard
from src.gamelogic.card.NumberCard import NumberCard
from src.gamelogic.card.RestartCard import RestartCard
from src.gamelogic.card.SelectionCard import SelectionCard
from src.gamelogic.card.ViewCard import ViewCard
from src.gamelogic.game.Game import Game


class DataConvert:

# TODO / WIP
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

# TODO / WIP

    # TODO: Mittels "game.active_player" prüfen, ob es das Client-Paket vom aktiven Spieler ist
    '''
    def net_to_gamelogic(self, input_dict, game):
        """
        Prüft die KartenIDs & Zusatzdaten, die der Client schickt

        :param game: Das Spiel, welches die Daten bekommt
        :param input_dict: Vom Client erstellte Dictionary
            "token": player id
            "selected_cards": card ids
            ggf. Wahlwerte bei SelectionCard:
                "chosen_number": zahl
                "chosen_color": farbe
        :return: Dictionary inklusive der entsprechenden Karten, die tatsächlich existieren
        """
        player = game.get_player_via_id(input_dict.get("token"))
        selected_cards = input_dict.get("selected_cards")
        checked_list = []
        output_dict = {
            "token": input_dict.get("token"),
            "game": game,
            "selected_cards": selected_cards
        }
        # Leer
        if len(selected_cards) == 0:
            return output_dict

        # Alle Werte Typ int
        if any(not isinstance(x, int) for x in selected_cards):
            game.disqualify_player(player, "Es dürfen nur Zahlen als IDs übergeben werden")
            return output_dict

        # Doppelte IDs
        if self.is_duplicate_ids(selected_cards):
            game.disqualify_player(player, "Die IDs enthalten Duplikate")
            return output_dict
        else:
            # ID in Spielerhand
            if self.is_list_in_player_hand(selected_cards, game):
                build_cards_list = self.build_card_objects(selected_cards, game)
                input_dict["selected_cards"] = build_cards_list
                # Nur SelectionCard
                if self.is_only_selection_card(input_dict.get("selected_cards")):
                    self.execute_steps_for_selection_card(input_dict, game)
            # ID nicht in Spielerhand
            else:
                # Spieler wegen falscher ID disqualifizieren
                game.disqualify_player(player, "ID existiert nicht in der Spielerhand")
        output_dict["selected_cards"] = checked_list
        return output_dict
    '''

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
                    game.disqualify_player(player, "Es wurden falsche Wahlwerte für die einfarbige SelectionCard übergeben")
            # Dict besitzt nicht Wahlwert
            else:
                game.disqualify_player(player, "Der Schlüssel 'chosen_number' befand sich nicht im dictionary")

        # Vierfarbig
        elif len(selection_card.color) == 4 and "chosen_number" in modified_input_dict and "chosen_color" in modified_input_dict:
            if modified_input_dict.get("chosen_number") in allowed_numbers and modified_input_dict.get("chosen_color") in allowed_colors:
                # Theoretical Card setzen
                number = modified_input_dict.get("chosen_number")
                color = modified_input_dict.get("chosen_color")
                selection_card.set_theoretical_card(number, color)
            else:
                # Spieler wegen falschen Wahlwerten disqualifizieren
                game.disqualify_player(player, "Es wurden falsche Wahlwerte für die vierfarbige SelectionCard übergeben")

        return modified_input_dict

    def is_data_from_active_player(self, token, game):
        return game.active_player.id == token


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

    def is_duplicate_ids(self, list_of_ids):
        """
        Überprüft, ob in der Liste doppelte Werte vorkommen

        :param list_of_ids: Liste von ids, die jeweils eine Karte repräsentieren
        :return: boolean
        """
        return len(list_of_ids) != len(set(list_of_ids))

    def is_only_selection_card(self, list):
        return len(list) == 0 and isinstance(list[0], SelectionCard)