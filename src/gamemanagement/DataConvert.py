from src.gamelogic.card.JokerCard import JokerCard
from src.gamelogic.card.NumberCard import NumberCard
from src.gamelogic.card.RestartCard import RestartCard
from src.gamelogic.game.Game import Game


class DataConvert:

    def gamelogic_to_net(self, game):

        turn_data = {}
        current_turn = game.turns[-1]
        if len(game.turns) == 1:
            opponent = game.player_2
            if isinstance(current_turn.top_card, (NumberCard, JokerCard, RestartCard)):
                turn_data = {
                    "previous_selected_cards": [],
                    "top_card": current_turn.top_card,
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



    def net_to_gamelogic(self, input_dict, game):
        """
        Prüft, ob die vom Spieler ausgewählten Karten im Spiel existieren.

        :param game: Das Spiel, welches die Daten bekommt
        :param input_dict: Vom Client erstellte Dictionary mit token/card ids
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
        if len(selected_cards) == 0:
            return output_dict
        if any(not isinstance(x, int) for x in selected_cards):
            game.set_disqualified_player(player)
            game.set_reason_of_disqualification("Es dürfen nur Zahlen als IDs übergeben werden")
            return output_dict
        if self.is_duplicate_ids(selected_cards):
            game.set_disqualified_player(player)
            game.set_reason_of_disqualification("Die IDs enthalten Duplikate")
            return output_dict
        else:
            for s_id in selected_cards:
                # Wenn eine der übergebenen IDs nicht in der Hand des
                # Spielers vorkommen, der die IDs geschickt hat,
                # ... ist die übergebene Liste ungültig
                card_to_check = game.deck.cards_dict.get(s_id)
                if card_to_check not in game.active_player.hand:
                    game.set_disqualified_player(player)
                    game.set_reason_of_disqualification(f"Die Karte mit der id {s_id} "
                                    f"existiert nicht in der Hand des Spielers, der die Karte geschickt hat")
                # Wenn die übergebene Liste gültig ist, werden die Karten
                # mit den entsprechenden IDs returnt
                else:
                    checked_list.append(card_to_check)
        output_dict["selected_cards"] = checked_list
        return output_dict

    def is_duplicate_ids(self, list_of_ids):
        """
        Überprüft, ob in der Liste doppelte Werte vorkommen

        :param list_of_ids: Liste von ids, die jeweils eine Karte repräsentieren
        :return: boolean
        """
        return len(list_of_ids) != len(set(list_of_ids))