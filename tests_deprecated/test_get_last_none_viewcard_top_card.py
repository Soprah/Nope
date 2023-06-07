import unittest

from src.gamelogic.card.JokerCard import JokerCard
from src.gamelogic.card.NumberCard import NumberCard
from src.gamelogic.card.RestartCard import RestartCard
from src.gamelogic.card.SelectionCard import SelectionCard
from src.gamelogic.card.ViewCard import ViewCard
from src.gamelogic.game.Game import Game
from src.gamelogic.player.Player import Player


class TestGetLastNoneViewCardTopCard(unittest.TestCase):
    def setUp(self):
        self.game = Game(Player("Eric", 3), Player("Marc", 19))
        self.n = NumberCard(1, ("red"), 2)
        self.j = JokerCard(2)
        self.r = RestartCard(3)
        self.s = SelectionCard(5, ("yellow"))
        self.v_1 = ViewCard(4, ("blue"))
        self.v_2 = ViewCard(5, ("green"))

    def test_get_last_none_viewcard_top_card_return_card(self):
        l = [self.n, self.j, self.r, self.v_1, self.v_2]
        self.game.deck.discard_stack = l
        card = self.game.get_last_none_viewcard_top_card()
        self.assertEqual(card, self.r)

        l = [self.n, self.r, self.v_1, self.j, self.v_2]
        self.game.deck.discard_stack = l
        card = self.game.get_last_none_viewcard_top_card()
        self.assertEqual(card, self.j)

    def test_get_last_none_viewcard_top_card_return_none(self):
        l = [self.v_1, self.v_2]
        self.game.deck.discard_stack = l
        card = self.game.get_last_none_viewcard_top_card()
        self.assertIsNone(card)

        l = [self.v_2]
        self.game.deck.discard_stack = l
        card = self.game.get_last_none_viewcard_top_card()
        self.assertIsNone(card)



if __name__ == '__main__':
    unittest.main()
