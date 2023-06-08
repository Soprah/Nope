import unittest

from src.gamelogic.card.SelectionCard import SelectionCard
from src.gamelogic.game.Game import Game
from src.gamelogic.player.Player import Player
from src.gamemanagement.DataConvert import DataConvert

class TestDataConvertExecuteStepsForSelectionCard(unittest.TestCase):

    def setUp(self):
        self.dc = DataConvert()
        self.p1 = Player("Eric", 33)
        self.p2 = Player("Marc", 99)
        self.game = Game(self.p1, self.p2)

    # Einfarbige SelectionCard - (Richtige) Werte vorhanden
    def test_execute_steps_for_singlecolor_selection_card_correct_chosen_values(self):
        # SelectionCard: id=97, color=("green",)
        card = self.game.deck.cards_dict.get(97)
        self.p1.hand = [card]
        client_dict = {
            "token": 33,
            "selected_cards": [card.id],
            "chosen_number": 2
        }
        expected_output_dict = {
            "token": 33,
            "selected_cards": [card]
        }

        # Entspricht die ID dem Spieler?
        self.assertEqual(self.p1.id, 33)
        player = self.game.get_player_via_id(33)
        self.assertEqual(self.p1, player)

        # Prüft die Anzahl der dict-schlüssel
        self.assertEqual(len(client_dict), 3)

        # Holt die ids
        id_list = client_dict.get("selected_cards")
        self.assertTrue(self.dc.is_list_in_player_hand(id_list, self.game))

        # Baut die Kartenobjekte
        cards = self.dc.build_card_objects(id_list, self.game)

        # Modifiziert das client dict für die übergabe
        client_dict["selected_cards"] = cards
        checked_dict = self.dc.execute_steps_for_selection_card(client_dict, self.game)

        # Speichert die selection card die chosen_number?
        number = card.get_number()
        self.assertEqual(number, 2)

        # Wurde "chosen_number" aus dem dict gelöscht?
        self.assertEqual(len(client_dict), 2)

        # Ist das neue dict wie gewünscht?
        self.assertDictEqual(client_dict, expected_output_dict)

    # Einfarbige SelectionCard - (Falsche) Werte vorhanden
    def test_execute_steps_for_singlecolor_selection_card_wrong_chosen_values(self):
        # SelectionCard: id=97, color=("green",)
        card = self.game.deck.cards_dict.get(97)
        self.p1.hand = [card]
        client_dict = {
            "token": 33,
            "selected_cards": [card.id],
            "chosen_number": 7
        }
        expected_output_dict = {
            "token": 33,
            "selected_cards": [card]
        }

        # Holt die ids
        self.assertEqual(self.p1.id, 33)
        id_list = client_dict.get("selected_cards")
        self.assertTrue(self.dc.is_list_in_player_hand(id_list, self.game))

        # Baut die Kartenobjekte
        cards = self.dc.build_card_objects(id_list, self.game)

        # Modifiziert das client dict für die übergabe
        client_dict["selected_cards"] = cards
        checked_dict = self.dc.execute_steps_for_selection_card(client_dict, self.game)

        # Wurde der Spieler erfolgreich disqualifiziert?
        player_token = checked_dict.get("token")
        player = self.game.get_player_via_id(player_token)
        self.assertEqual(self.p1, player)
        self.assertTrue(self.p1.is_disqualified)

        # Richtiger Grund für die Disqualifizierung?
        self.assertEqual(self.game.reason_of_disqualification , "Es wurden falsche Wahlwerte für die einfarbige SelectionCard übergeben")

    # Einfarbige SelectionCard - Werte nicht vorhanden
    def test_execute_steps_for_singlecolor_selection_card_missing_chosen_values(self):
        # SelectionCard: id=97, color=("green",)
        card = self.game.deck.cards_dict.get(97)
        self.p1.hand = [card]
        client_dict = {
            "token": 33,
            "selected_cards": [card.id],
            # "chosen_number": 2
        }
        expected_output_dict = {
            "token": 33,
            "selected_cards": [card]
        }

        # Holt die ids
        self.assertEqual(self.p1.id, 33)
        id_list = client_dict.get("selected_cards")
        self.assertTrue(self.dc.is_list_in_player_hand(id_list, self.game))

        # Baut die Kartenobjekte
        cards = self.dc.build_card_objects(id_list, self.game)

        # Modifiziert das client dict für die übergabe
        client_dict["selected_cards"] = cards
        checked_dict = self.dc.execute_steps_for_selection_card(client_dict, self.game)

        # Wurde der Spieler erfolgreich disqualifiziert?
        player_token = checked_dict.get("token")
        player = self.game.get_player_via_id(player_token)
        self.assertEqual(self.p1, player)
        self.assertTrue(self.p1.is_disqualified)

        # Richtiger Grund für die Disqualifizierung?
        self.assertEqual(self.game.reason_of_disqualification , "Der Schlüssel 'chosen_number' befand sich nicht im dictionary")


    # Mehrfarbige SelectionCard - (Richtige) Werte vorhanden
    def test_execute_steps_for_multicolor_selection_card_correct_chosen_values(self):
        # SelectionCard: id=97, color=("green",)
        card = self.game.deck.cards_dict.get(97)
        self.p1.hand = [card]
        client_dict = {
            "token": 33,
            "selected_cards": [card.id],
            "chosen_number": 2,
            "chosen_color": ("blue",)
        }
        expected_output_dict = {
            "token": 33,
            "selected_cards": [card]
        }

        # Entspricht die ID dem Spieler?
        self.assertEqual(self.p1.id, 33)
        player = self.game.get_player_via_id(33)
        self.assertEqual(self.p1, player)

        # Prüft die Anzahl der dict-schlüssel
        self.assertEqual(len(client_dict), 4)

        # Holt die ids
        id_list = client_dict.get("selected_cards")
        self.assertTrue(self.dc.is_list_in_player_hand(id_list, self.game))

        # Baut die Kartenobjekte
        cards = self.dc.build_card_objects(id_list, self.game)

        # Modifiziert das client dict für die übergabe
        client_dict["selected_cards"] = cards
        checked_dict = self.dc.execute_steps_for_selection_card(client_dict, self.game)
        edited_card = checked_dict.get("selected_cards")[0]

        # Speichert die selection card die chosen_number?
        number = edited_card.get_number()
        self.assertEqual(number, 2)

        # Speichert die selection card die chosen_color?
        color = edited_card.get_color()
        self.assertEqual(color, ("blue",))

        # Wurde "chosen_number" aus dem dict gelöscht?
        self.assertEqual(len(client_dict), 2)

        # Ist das neue dict wie gewünscht?
        self.assertDictEqual(client_dict, expected_output_dict)

    # Mehrfarbige SelectionCard - (Falsche) Werte vorhanden
    # Mehrfarbige SelectionCard - Werte nicht vorhanden

if __name__ == '__main__':
    unittest.main()
