import uuid

from src.gamelogic.deck.Deck import Deck
from src.gamelogic.game.GameState import NewTurnState
from src.gamelogic.player.Player import Player
from src.gamelogic.turn.Turn import Turn

class Game:

    def __init__(self, p1, p2):
        self.id = uuid.uuid4()
        self.state = NewTurnState()
        self.turns = []
        self.deck = Deck()
        self.player_1 = p1
        self.player_2 = p2
        self.deck.initialize_discard_stack()
        self.assign_deck_to_players()
        self.pass_first_cards()
        self.active_player = self.player_1
        self.winner = None
        self.reason_of_disqualification = None

    def execute(self, data=None):
        return self.state.handle(self, data)

    def change_state(self):
        self.state.change_state(self)

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def switch_active_player(self):
        if self.active_player == self.player_1:
            self.active_player = self.player_2
        else:
            self.active_player = self.player_1

    def disqualify_player(self, player, reason):
        self.set_disqualified_player(player)
        self.set_reason_of_disqualification(reason)

    def set_disqualified_player(self, disqualified_player):
        if disqualified_player == self.player_1 or disqualified_player == self.player_2 and isinstance(disqualified_player, Player):
            disqualified_player.is_disqualified = True

    def set_reason_of_disqualification(self, reason):
        self.reason_of_disqualification = reason

    def get_player_via_id(self, id):
        if self.player_1.id == id:
            return self.player_1
        elif self.player_2.id == id:
            return self.player_2
        else:
            raise ValueError("Es gibt keinen Spieler in dem Spiel mit dieser ID !")

    def assign_deck_to_players(self):
        self.player_1.set_deck(self.deck)
        self.player_2.set_deck(self.deck)

    def pass_first_cards(self):
        amount_start_cards = 8
        for i in range(amount_start_cards):
            self.player_1.draw_card()
            self.player_2.draw_card()

    def next_turn(self):
        if self.is_game_over():
            self.finish_game()
        elif len(self.turns) == 0:
            new_turn = Turn(self.active_player, self.deck.discard_stack[-1])
            self.turns.append(new_turn)
            return new_turn
        else:
            self.switch_active_player()
            new_turn = Turn(self.active_player, self.deck.discard_stack[-1])
            self.turns.append(new_turn)
            return new_turn

    def make_move(self):
        cards_current_turn = self.turns[-1].selected_cards
        if len(cards_current_turn) == 0:
            print("NOPE")
        elif len(cards_current_turn) > 0:
            for card in cards_current_turn:
                self.active_player.discard_card(card)
        else:
            print("something went wrong")
        return cards_current_turn

    def is_game_over(self):
        return len(self.player_1.hand) == 0 or len(self.player_2.hand) == 0 or self.player_1.is_disqualified or self.player_2.is_disqualified

    def finish_game(self):
        if len(self.player_1.hand) == 0 or self.player_1.is_disqualified:
            self.winner = self.player_2
        elif len(self.player_2.hand) == 0 or self.player_2.is_disqualified:
            self.winner = self.player_1
        else:
            print("No winner yet")
        print(f"Anzahl der Runden {len(self.turns)}")
        print("PLACEHOLDER FOR SENDING DATA TO THE DATABASE")
        return "GAME END"

    """
    def run(self):
        while self.is_game_over() == False:
            print("**********************")
            # 1. Turnobjekt erstellen
            new_turn = self.next_turn()
            print(f"Turn Nr. {len(self.turns)}")
            print("Spielzug von: ", self.active_player.name)
            game_sent_turn_data = self.send_turn_data(new_turn)

            # 1-b. Daten ausgeben (Spielerhand, Top Karte)
            print("Anzahl der Karten in Spielerhand", len(self.active_player.hand))
            for card in game_sent_turn_data.get("own_hand_cards"):
                print(f"Spielerkarte: {card}")
            print(f"Top Karte des aktuellen Turns {self.turns[-1].top_card}")

            # 2. Client empfängt und verarbeitet Daten
            client_processed_turn_data = self.active_player.CS_select_cards(game_sent_turn_data)

            # 2-b. Ausgewählte Karten des Clients ausgeben
            print("Das Dictionary vom Client: ", client_processed_turn_data)
            if len(client_processed_turn_data .get("selected_cards")) != 0:
                for card in client_processed_turn_data .get("selected_cards"):
                    print("Ausgewählte Karte/ID: ", card)

            # 3. Server empfängt Daten vom Client
            checked_list = self.receive_turn_data(client_processed_turn_data)

            # 3-b. Die IDs der ausgewählten Karten ausgeben
            print("Länge der gecheckten Liste: ", len(checked_list))
            for item in checked_list:
                print(item)

            # 4. Spielzug nach Validität prüfen
            turn_valid = self.turns[-1].is_valid(checked_list)

            # 4-b. Validität ausgeben
            print(f"War der Zug vom Spieler valide? {turn_valid}")

            # 5. Prüfen, ob der Spieler noch einen Spielzug ausführen muss
            another_attempt_necessary = self.turns[-1].is_another_attempt_necessary()

            # 5-b. Validität ausgeben
            print(f"Muss der Spieler noch einen Spielzug machen? {another_attempt_necessary}")
            if turn_valid and another_attempt_necessary:
                print("Der Spieler macht noch einen Spielzug und zieht zwei Karten")
                # X-1: Spieler zieht zwei Karten
                self.active_player.draw_card()
                self.active_player.draw_card()

                # X-2: Daten verpacken zum Senden
                second_game_sent_turn_data = self.send_turn_data(self.turns[-1])

                # X-2-b: Neuen Daten ausgeben (Neue Spielerhand)
                for card in self.active_player.hand:
                    print(f"Spielerkarte: {card}")
                second_client_processed_turn_data = self.active_player.CS_select_cards(second_game_sent_turn_data)
                print("Der Spieler versucht es erneut")
                print("Das Dictionary vom Client: ", second_client_processed_turn_data)
                if len(second_client_processed_turn_data.get("selected_cards")) != 0:
                    for card in second_client_processed_turn_data.get("selected_cards"):
                        print("Ausgewählte Karte/ID: ", card)
                second_checked_list = self.receive_turn_data(second_client_processed_turn_data)
                print("Länge der gecheckten Liste: ", len(second_checked_list))
                for item in second_checked_list:
                    print(item)
                second_turn_valid = self.turns[-1].is_valid(second_checked_list)
                print("Ist der Spielzug gültig?", second_turn_valid)
                if second_turn_valid:
                    discarded_cards = self.make_move()
                    print("Ablegte Karten Anzahl: ", len(discarded_cards))
                    if len(discarded_cards) > 0:
                        for c in discarded_cards:
                            print("Abgelegte Karte: ", c)
                        print("Anzahl der Karten in Spielerhand nach Ablegen", len(self.active_player.hand))
                        print("Spielerhand nach Ablegen:")
                        for c in self.active_player.hand:
                            print("Karte: ", c)
            else:
                discarded_cards = self.make_move()
                print("Ablegte Karten Anzahl: ", len(discarded_cards))
                if len(discarded_cards) > 0:
                    for c in discarded_cards:
                        print("Abgelegte Karte: ", c)

                print("Anzahl der Karten in Spielerhand nach Ablegen", len(self.active_player.hand))
                print("Spielerhand nach Ablegen:")
                for c in self.active_player.hand:
                    print("Karte: ", c)
        print("\n")
        print("\n")
        self.finish_game()
        print("WINNER: ", self.winner)
    """

    def __str__(self) -> str:
        return f"Game ID: {self.id}, ID von Player 1: {self.player_1.get_id()}, ID von Player 2: {self.player_2.get_id()}"

    def __repr__(self):
        return f"Game ID: {self.id}, ID von Player 1: {self.player_1.get_id()}, ID von Player 2: {self.player_2.get_id()}"