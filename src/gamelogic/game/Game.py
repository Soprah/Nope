from src.gamelogic.deck.Deck import Deck
from src.gamelogic.player.Player import Player
from src.gamelogic.turn.Turn import Turn

class Game:

    def __init__(self, player_1_name, player_2_name):
        self.setup(player_1_name, player_2_name)
        '''
        self.deck = Deck()
        self.player_1 = Player(self.deck, player_1_name)
        self.player_2 = Player(self.deck, player_2_name)
        self.active_player = None
        self.turns = []
        self.deck.initialize_discard_stack()
        self.pass_first_cards()
        self.set_active_player()
        '''
    # '''
    def setup(self, player_1_name, player_2_name):
        self.turns = []
        self.deck = Deck()
        self.player_1 = Player(self.deck, player_1_name)
        self.player_2 = Player(self.deck, player_2_name)
        self.deck.initialize_discard_stack()
        self.pass_first_cards()
        self.set_active_player()
    # '''

    def set_active_player(self):
        if len(self.turns) == 0:
            self.active_player = self.player_1
        elif self.active_player == self.player_1:
            self.active_player = self.player_2
        else:
            self.active_player = self.player_1

    def pass_first_cards(self):
        amount_start_cards = 8
        for i in range(amount_start_cards):
            self.player_1.draw_card()
            self.player_2.draw_card()

    # '''
    def send_turn_data(self, current_turn):
        turn_data = {}
        if len(self.turns) == 0:
            opponent = self.player_2
            turn_data = {
                "previous_selected_cards": self.deck.discard_stack[-1],
                "amount_opponent_cards": len(opponent.hand),
                "own_hand_cards": current_turn.player.hand
            }
        '''
        elif len(self.turns) > 0:
            previous_turn = self.turns[-1]
            if isinstance(previous_turn, Turn) and isinstance(current_turn, Turn):
                turn_data = {
                    "previous_selected_cards": previous_turn.selected_cards,
                    "amount_opponent_cards": len(previous_turn.player.hand),
                    "own_hand_cards": current_turn.player.hand
                }
        '''
        return turn_data
    # '''






