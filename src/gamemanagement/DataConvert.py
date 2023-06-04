from src.gamelogic.game.Game import Game


class DataConvert:

    def net_to_gamelogic(self, input_dict, game):
        """
        Prüft, ob die vom Spieler ausgewählten Karten im Spiel existieren.

        :param game: Das Spiel, welches die Daten bekommt
        :param input_dict: Liste von ids der übergebenen Karten
        :return: Liste der entsprechenden Karten, die tatsächlich existieren
        """
        selected_cards = dict.get("selected_cards")
        checked_list = []
        output_dict = {"token": input_dict.get("token")}
        if len(selected_cards) == 0:
            return checked_list
        if any(not isinstance(x, int) for x in selected_cards):
            raise TypeError("Es dürfen nur Zahlen als IDs übergeben werden!")
        if self.is_duplicate_ids(selected_cards):
            raise ValueError("Die IDs enthalten Duplikate")
        else:
            for s_id in selected_cards:
                # Wenn eine der übergebenen IDs nicht in der Hand des Spielers vorkommen, der die IDs geschickt hat,
                # ... ist die übergebene Liste ungültig
                card_to_check = game.deck.cards_dict.get(s_id)
                if card_to_check not in game.active_player.hand:
                    raise ValueError(f"Die Karte mit der id {s_id} existiert nicht "
                                     f"in der Hand des Spielers, der die Karte geschickt hat")
                # Wenn die übergebene Liste gültig ist, werden die Karten mit den entsprechenden IDs returnt
                else:
                    checked_list.append(card_to_check)
        output_dict["selected_cards"] = checked_list
        output_dict["game"] = game
        return output_dict

    def is_duplicate_ids(self, list_of_ids):
        """
        Überprüft, ob in der Liste doppelte Werte vorkommen

        :param list_of_ids: Liste von ids, die jeweils eine Karte repräsentieren
        :return: boolean
        """
        return len(list_of_ids) != len(set(list_of_ids))