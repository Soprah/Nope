import unittest

from src.gamelogic.card.NumberCard import NumberCard
from src.gamelogic.game.Game import Game
from src.gamelogic.player.Player import Player


class TestGamelogicToNet(unittest.TestCase):
    def setUp(self):
        self.p1 = Player("Eric", 3)
        self.p2 = Player("Marc", 19)
        self.game = Game(self.p1, self.p2)

    # TODO
    #   * Keine Objekte
    #   * Sondern das richtige dict-paket

    # def test_send_turn_data_game_start_numbercard_top_card(self):
    #     card = NumberCard(1, ("red", "blue"), 2)
    #     self.game.deck.discard_stack[-1] = card
    #     turn = self.game.next_turn()
    #     actual_turn_data = self.game.send_turn_data(current_turn=turn)
    #     self.assertEqual(actual_turn_data.get("previous_selected_cards"), [])
    #     self.assertEqual(actual_turn_data.get("top_card"), card)
    #     self.assertEqual(actual_turn_data.get("top_card"), turn.top_card)
    #     self.assertEqual(actual_turn_data.get("amount_opponent_cards"), len(self.game.player_2.hand))
    #     self.assertEqual(actual_turn_data.get("own_hand_cards"), self.game.player_1.hand)

if __name__ == '__main__':
    unittest.main()
