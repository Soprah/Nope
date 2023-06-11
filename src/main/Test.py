from src.gamelogic.card.SelectionCard import SelectionCard
from src.gamelogic.card.ViewCard import ViewCard
from src.gamelogic.game.Game import Game
from src.gamelogic.player.Player import Player
from src.dataconvert.DataConvert import DataConvert

# dc = DataConvert()
p1 = Player("Eric", 33)
p2 = Player("Marc", 19)
game = Game(p1, p2)
for c in game.deck.cards:
    print(c)

view_red = game.deck.cards_dict.get(91)
if isinstance(view_red, ViewCard):
    print("OK!")


# c1 = game.deck.cards_dict.get(71)
# c2 = game.deck.cards_dict.get(80)
# set_c1 = set(c1.color)
# set_c2 = set(c2.color)
#
# common = (set_c1 & set_c2)
# t_common = tuple(common)
# print(t_common)

    """
    def setUp(self):

        # Alte Tests
        self.deck = Deck()
        self.player = Player(self.deck, "eric")

        # Neue Tests

        # Spielvorbereitung
        self.p1 = Player("Christina", 8)
        self.p2 = Player("Marc", 19)
        self.game = Game(self.p1, self.p2)

        # Karten
        self.g_1 = self.game.deck.cards_dict.get(5)
        self.y_1 = self.game.deck.cards_dict.get(7)
        self.b_1 = self.game.deck.cards_dict.get(4)
        self.view_red = self.game.deck.cards_dict.get(91)
        # self.view_red.clear_theoretical_card()
        self.y_3 = self.game.deck.cards_dict.get(20)
        self.g_2 = self.game.deck.cards_dict.get(14)
        self.y_2 = self.game.deck.cards_dict.get(16)
        self.selection_blue = self.game.deck.cards_dict.get(96)

        self.g_3 = self.game.deck.cards_dict.get(19)
    def test_is_valid_case_A_6(self):
        p1_hand = [
            self.g_1,
            self.y_1,
            self.b_1,
            self.g_3,
            self.y_3,
            self.g_2,
            self.y_2,
            self.selection_blue
        ]
        self.assertIs(self.view_red, ViewCard)
    """