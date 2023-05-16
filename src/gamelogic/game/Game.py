import uuid

from src.gamelogic.deck.Deck import Deck
from src.gamelogic.player.Player import Player
from src.gamelogic.turn.Turn import Turn

class Game:

    def __init__(self, p1, p2):
        self.setup(p1, p2)

    def setup(self, p1, p2):
        self.id = uuid.uuid4()
        self.turns = []
        self.deck = Deck()
        self.player_1 = p1
        self.player_2 = p2
        self.deck.initialize_discard_stack()
        self.assign_deck_to_players()
        self.pass_first_cards()
        self.active_player = self.player_1
        self.winner = None

    def switch_active_player(self):
        if self.active_player == self.player_1:
            self.active_player = self.player_2
        else:
            self.active_player = self.player_1

    # def set_active_player(self):
    #     if len(self.turns) == 0:
    #         self.active_player = self.player_1
    #     elif self.active_player == self.player_1:
    #         self.active_player = self.player_2
    #     else:
    #         self.active_player = self.player_1

    def assign_deck_to_players(self):
        self.player_1.set_deck(self.deck)
        self.player_2.set_deck(self.deck)

    def pass_first_cards(self):
        amount_start_cards = 8
        for i in range(amount_start_cards):
            self.player_1.draw_card()
            self.player_2.draw_card()

    # '''
    def send_turn_data(self, current_turn):
        """
        Übergibt die notwendigen turn_data an dem Spieler, der aktuell am Zug ist.

        :param current_turn: der aktuelle Zug und seine Daten
        :return: turn_data
        """
        turn_data = {}
        if len(self.turns) == 1:
            opponent = self.player_2
            turn_data = {
                "previous_selected_cards": [],
                "top_card": self.deck.discard_stack[-1],
                "amount_opponent_cards": len(opponent.hand),
                "own_hand_cards": current_turn.player.hand
            }
        # '''
        elif len(self.turns) > 1:
            previous_turn = self.turns[-1]
            if isinstance(previous_turn, Turn) and isinstance(current_turn, Turn):
                turn_data = {
                    "previous_selected_cards": previous_turn.selected_cards,
                    "top_card": previous_turn.top_card,
                    "amount_opponent_cards": len(previous_turn.player.hand),
                    "own_hand_cards": current_turn.player.hand
                }
        # '''
        return turn_data
    # '''

    def receive_turn_data(self, dict_selected_cards):
        """
        Prüft, ob die vom Spieler ausgewählten Karten im Spiel existieren.

        :param dict_selected_cards: Liste von ids der übergebenen Karten
        :return: Liste der entsprechenden Karten, die tatsächlich existieren
        """
        selected_cards = dict_selected_cards.get("selected_cards")
        checked_list = []
        if len(selected_cards) == 0:
            return checked_list
        if any(not isinstance(x, int) for x in selected_cards):
            raise TypeError("Es dürfen nur Zahlen als IDs übergeben werden!")
        if self.is_duplicate_ids(selected_cards) == True:
            raise ValueError("Die IDs enthalten Duplikate")
        else:
            for s_id in selected_cards:
                # Wenn eine der übergebenen IDs nicht in der Hand des Spielers vorkommen, der die IDs geschickt hat,
                # ... ist die übergebene Liste ungültig
                card_to_check = self.deck.cards_dict.get(s_id)
                if card_to_check not in self.active_player.hand:
                    raise ValueError(f"Die Karte mit der id {s_id} existiert nicht "
                                     f"in der Hand des Spielers, der die Karte geschickt hat")
                # Wenn die übergebene Liste gültig ist, werden die Karten mit den entsprechenden IDs returnt
                else:
                    checked_list.append(card_to_check)
        return checked_list

    def is_duplicate_ids(self, list_of_ids):
        """
        Überprüft, ob in der Liste doppelte Werte vorkommen

        :param list_of_ids: Liste von ids, die jeweils eine Karte repräsentieren
        :return: boolean
        """
        return len(list_of_ids) != len(set(list_of_ids))

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

    def __str__(self) -> str:
        return f"Game ID: {self.id}, ID von Player 1: {self.player_1.get_id()}, ID von Player 2: {self.player_2.get_id()}"