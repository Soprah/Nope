import unittest

from src.gamelogic.card.JokerCard import JokerCard
from src.gamelogic.card.NumberCard import NumberCard
from src.gamelogic.card.RestartCard import RestartCard
from src.gamelogic.card.SelectionCard import SelectionCard
from src.gamelogic.card.ViewCard import ViewCard
from src.gamelogic.game.Game import Game
from src.gamelogic.player.Player import Player
from src.gamelogic.turn.Turn import Turn


class TestGameSendTurnData(unittest.TestCase):
    def setUp(self):
        self.p1 = Player("Eric", 3)
        self.p2 = Player("Marc", 19)
        self.game = Game(self.p1, self.p2)

    def test_send_turn_data_game_start_numbercard_top_card(self):
        card = NumberCard(1, ("red", "blue"), 2)
        self.game.deck.discard_stack[-1] = card
        turn = self.game.next_turn()
        actual_turn_data = self.game.send_turn_data(current_turn=turn)
        self.assertEqual(actual_turn_data.get("previous_selected_cards"), [])
        self.assertEqual(actual_turn_data.get("top_card"), card)
        self.assertEqual(actual_turn_data.get("top_card"), turn.top_card)
        self.assertEqual(actual_turn_data.get("amount_opponent_cards"), len(self.game.player_2.hand))
        self.assertEqual(actual_turn_data.get("own_hand_cards"), self.game.player_1.hand)

    def test_send_turn_data_game_start_jokercard_top_card(self):
        card = JokerCard(1)
        self.game.deck.discard_stack[-1] = card
        turn = self.game.next_turn()
        turn.top_card = card
        actual_turn_data = self.game.send_turn_data(current_turn=turn)
        self.assertEqual(actual_turn_data.get("previous_selected_cards"), [])
        self.assertEqual(actual_turn_data.get("top_card"), card)
        self.assertEqual(actual_turn_data.get("top_card"), turn.top_card)
        self.assertEqual(actual_turn_data.get("amount_opponent_cards"), len(self.game.player_2.hand))
        self.assertEqual(actual_turn_data.get("own_hand_cards"), self.game.player_1.hand)

    def test_send_turn_data_game_start_restartcard_top_card(self):
        turn = self.game.next_turn()
        card = RestartCard(1)
        turn.top_card = card
        actual_turn_data = self.game.send_turn_data(current_turn=turn)
        self.assertEqual(actual_turn_data.get("previous_selected_cards"), [])
        self.assertEqual(actual_turn_data.get("top_card"), card)
        self.assertEqual(actual_turn_data.get("top_card"), turn.top_card)
        self.assertEqual(actual_turn_data.get("amount_opponent_cards"), len(self.game.player_2.hand))
        self.assertEqual(actual_turn_data.get("own_hand_cards"), self.game.player_1.hand)

    def test_send_turn_data_game_start_viewcard_top_card(self):
        card = ViewCard(1, ("blue"))
        self.game.deck.discard_stack[-1] = card
        turn = self.game.next_turn()
        turn.top_card = card
        actual_turn_data = self.game.send_turn_data(current_turn=turn)
        self.assertEqual(len(actual_turn_data), 5)
        self.assertEqual(actual_turn_data.get("previous_selected_cards"), [])
        self.assertEqual(actual_turn_data.get("top_card"), card)
        self.assertEqual(actual_turn_data.get("top_card"), turn.top_card)
        self.assertEqual(actual_turn_data.get("amount_opponent_cards"), len(self.game.player_2.hand))
        self.assertEqual(actual_turn_data.get("own_hand_cards"), self.game.player_1.hand)
        self.assertIsNone(actual_turn_data.get("under_top_card"))

    def test_send_turn_data_game_start_one_color_selectioncard_top_card(self):
        card = SelectionCard(1, ("blue"))
        self.game.deck.discard_stack[-1] = card
        turn = self.game.next_turn()
        turn.top_card = card
        actual_turn_data = self.game.send_turn_data(current_turn=turn)
        self.assertEqual(len(actual_turn_data), 5)
        self.assertEqual(actual_turn_data.get("previous_selected_cards"), [])
        self.assertEqual(actual_turn_data.get("top_card"), card)
        self.assertEqual(actual_turn_data.get("top_card"), turn.top_card)
        self.assertEqual(actual_turn_data.get("amount_opponent_cards"), len(self.game.player_2.hand))
        self.assertEqual(actual_turn_data.get("own_hand_cards"), self.game.player_1.hand)
        self.assertIsNone(actual_turn_data.get("choice_number"))

    def test_send_turn_data_game_start_four_color_selectioncard_top_card(self):
        card = SelectionCard(1, (("red"), ("blue"), ("yellow"), ("green")))
        self.game.deck.discard_stack[-1] = card
        turn = self.game.next_turn()
        turn.top_card = card
        actual_turn_data = self.game.send_turn_data(current_turn=turn)
        self.assertEqual(len(actual_turn_data), 6)
        self.assertEqual(actual_turn_data.get("previous_selected_cards"), [])
        self.assertEqual(actual_turn_data.get("top_card"), card)
        self.assertEqual(actual_turn_data.get("top_card"), turn.top_card)
        self.assertEqual(actual_turn_data.get("amount_opponent_cards"), len(self.game.player_2.hand))
        self.assertEqual(actual_turn_data.get("own_hand_cards"), self.game.player_1.hand)
        self.assertIsNone(actual_turn_data.get("choice_number"))

    """ Spielsimulation | Spielstart - Zufällige Karte liegt auf dem Ablagestapel """
    def test_send_turn_data_game_start_random_top_card(self):
        turn = self.game.next_turn()
        if isinstance(turn.top_card, NumberCard):
            actual_turn_data = self.game.send_turn_data(current_turn=turn)
            self.assertEqual(len(actual_turn_data), 4)
            self.assertEqual(actual_turn_data.get("previous_selected_cards"), [])
            self.assertEqual(actual_turn_data.get("top_card"), self.game.deck.discard_stack[-1])
            self.assertEqual(actual_turn_data.get("amount_opponent_cards"), len(self.game.player_2.hand))
            self.assertEqual(actual_turn_data.get("own_hand_cards"), self.game.player_1.hand)
        elif isinstance(turn.top_card, JokerCard):
            actual_turn_data = self.game.send_turn_data(current_turn=turn)
            self.assertEqual(len(actual_turn_data), 4)
            self.assertEqual(actual_turn_data.get("previous_selected_cards"), [])
            self.assertEqual(actual_turn_data.get("top_card"), self.game.deck.discard_stack[-1])
            self.assertEqual(actual_turn_data.get("amount_opponent_cards"), len(self.game.player_2.hand))
            self.assertEqual(actual_turn_data.get("own_hand_cards"), self.game.player_1.hand)
        elif isinstance(turn.top_card, RestartCard):
            actual_turn_data = self.game.send_turn_data(current_turn=turn)
            self.assertEqual(len(actual_turn_data), 4)
            self.assertEqual(actual_turn_data.get("previous_selected_cards"), [])
            self.assertEqual(actual_turn_data.get("top_card"), self.game.deck.discard_stack[-1])
            self.assertEqual(actual_turn_data.get("amount_opponent_cards"), len(self.game.player_2.hand))
            self.assertEqual(actual_turn_data.get("own_hand_cards"), self.game.player_1.hand)
        elif isinstance(turn.top_card, ViewCard):
            actual_turn_data = self.game.send_turn_data(current_turn=turn)
            self.assertEqual(len(actual_turn_data), 5)
            self.assertEqual(actual_turn_data.get("previous_selected_cards"), [])
            self.assertEqual(actual_turn_data.get("top_card"), self.game.deck.discard_stack[-1])
            self.assertEqual(actual_turn_data.get("amount_opponent_cards"), len(self.game.player_2.hand))
            self.assertEqual(actual_turn_data.get("own_hand_cards"), self.game.player_1.hand)
            self.assertIsNone(actual_turn_data.get("under_top_card"))
        elif isinstance(turn.top_card, SelectionCard) and len(turn.top_card.color) == 1:
            actual_turn_data = self.game.send_turn_data(current_turn=turn)
            self.assertEqual(len(actual_turn_data), 5)
            self.assertEqual(actual_turn_data.get("previous_selected_cards"), [])
            self.assertEqual(actual_turn_data.get("top_card"), self.game.deck.discard_stack[-1])
            self.assertEqual(actual_turn_data.get("amount_opponent_cards"), len(self.game.player_2.hand))
            self.assertEqual(actual_turn_data.get("own_hand_cards"), self.game.player_1.hand)
            self.assertIsNone(actual_turn_data.get("choice_number"))
        elif isinstance(turn.top_card, SelectionCard) and len(turn.top_card.color) == 4:
            actual_turn_data = self.game.send_turn_data(current_turn=turn)
            self.assertEqual(len(actual_turn_data), 6)
            self.assertEqual(actual_turn_data.get("previous_selected_cards"), [])
            self.assertEqual(actual_turn_data.get("top_card"), self.game.deck.discard_stack[-1])
            self.assertEqual(actual_turn_data.get("amount_opponent_cards"), len(self.game.player_2.hand))
            self.assertEqual(actual_turn_data.get("own_hand_cards"), self.game.player_1.hand)
            self.assertIsNone(actual_turn_data.get("choice_number"))
            self.assertIsNone(actual_turn_data.get("choice_single_color"))

    """ MUSS NOCH IMPLEMENTIERT WERDEN """
    # def test_send_turn_data_mid_game(self):
    #     pass

if __name__ == '__main__':
    unittest.main()