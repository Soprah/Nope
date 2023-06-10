import unittest

from src.dataconvert.DataConvert import DataConvert
from src.gamelogic.game.Game import Game
from src.gamelogic.player.Player import Player


class TestDataConvertToDictPreviousSelectedCards(unittest.TestCase):
    def setUp(self):
        self.p1 = Player("Christina", 8)
        self.p2 = Player("Marc", 19)
        self.game = Game(self.p1, self.p2)
        self.dc = DataConvert()

    # Jeder Kartentyp (Number, Joker, Restart, View, SingleSel, MultipleSel)
    # Turn obj erstellen
    # Diese karten dem turn obj attribut zuweisen
    # expected_output definieren
    # zu testende methode ausführen und erg auf actual_output speichern
    # expected und actual vergleichen

    # GAME START
    def test_to_dict_previous_selected_cards_game_start(self):
        expected_output = {}

        actual_output = self.dc.to_dict_previous_selected_cards(self.game)

        self.assertDictEqual(actual_output, expected_output)

    # MID GAME
    """
    def test_to_dict_previous_selected_cards_mid_game(self):
        # color=red | number=2
        n_card = self.game.deck.cards_dict.get(9)

        # color=red,blue,yellow,green | number=1
        j_card = self.game.deck.cards_dict.get(101)

        # color=red,blue,yellow,green | number=2
        r_card = self.game.deck.cards_dict.get(87)

        # color=blue | number=none
        v_card = self.game.deck.cards_dict.get(92)
        v_card.set_theoretical_card()  # muss ich das setzen?

        # color=red | number=2
        n_card = self.game.deck.cards_dict.get(9)
        # color=red | number=2
        n_card = self.game.deck.cards_dict.get(9)
        pass
    """



if __name__ == '__main__':
    unittest.main()
