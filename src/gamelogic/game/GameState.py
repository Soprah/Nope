from src.dataconvert.DataConvert import DataConvert


class GameState:

    dc = DataConvert()

    def handle(self, g):
        pass

    def __str__(self):
        return type(self).__name__

    def __repr__(self):
        return type(self).__name__


class NewTurnState(GameState):

    def handle(self, g, data=None):
        print("*** CLASS: ", self, " ***")

        # 1. Turnobjekt erstellen
        print("**********************")
        g.next_turn()
        self.print_turn_description(g)

        # 1-a. Paket erstellen
        output = self.dc.gamelogic_to_net(g)

        self.change_state(g)

        # 1-b. Daten ausgeben (Spielerhand, Top Karte)
        self.print_player_hand(g, output)
        self.print_turn_top_card(g)

        return output

    def change_state(self, g):
        g.set_state(FirstAttemptState())

    def __str__(self):
        return type(self).__name__

    def __repr__(self):
        return type(self).__name__

    def print_turn_description(self, g):
        print(f"Turn Nr. {len(g.turns)}")
        print("Spielzug von: ", g.active_player.name)

    def print_player_hand(self, g, output):
        print("Anzahl der Karten in Spielerhand", len(g.active_player.hand))
        for card in output.get("own_hand_cards"):
            print(f"Spielerkarte: {card}")

    def print_turn_top_card(self, g):
        print(f"Top Karte des aktuellen Turns | {g.turns[-1].top_card}")


class FirstAttemptState(GameState):

    def handle(self, g, data=None):

        print("*** CLASS: ", self, " ***")

        # 2-b. Ausgewählte Karten des Clients ausgeben
        print("Das Dictionary vom Client: ", data)
        if len(data.get("selected_cards")) != 0:
            for card in data.get("selected_cards"):
                print("Ausgewählte Karte/ID: ", card)

        # 3. Server empfängt Daten vom Client
        processed_data = self.dc.net_to_gamelogic(data, g)
        print("War der Spielzug des Clients ungültig: ", g.is_game_over())
        if g.is_game_over():
            print("Grund der Disqualifizierung: ", g.reason_of_disqualification)
            g.declare_winner_loser()
            return False

        # 3-b. Die IDs der ausgewählten Karten ausgeben
        cards = processed_data.get("selected_cards")
        print("Länge der gecheckten Liste inklusive Karten: ", len(cards))
        for item in cards:
            print(item)

        # 4. Spielzug nach Validität prüfen
        turn_valid = g.turns[-1].is_valid(cards)
        if not turn_valid:
            g.disqualify_player(g.active_player, "Invalider Spielzug..")
            g.declare_winner_loser()

        # 4-b. Validität ausgeben
        print(f"War der Zug vom Spieler valide? {turn_valid}")

        self.change_state(g)
        return turn_valid

    def __str__(self):
        return type(self).__name__

    def __repr__(self):
        return type(self).__name__

    def change_state(self, g):
        # 5. Prüfen, ob der Spieler noch einen Spielzug ausführen muss
        another_attempt_necessary = g.turns[-1].is_another_attempt_necessary()
        print(f"Muss Spieler {g.active_player.name} noch einen Spielzug machen? Antwort: {another_attempt_necessary}")
        if another_attempt_necessary:
            g.set_state(NewCardsState())
        else:
            g.set_state(FinishTurnState())


class FinishTurnState(GameState):

    def handle(self, g, data=None):
        print("*** CLASS: ", self, " ***")

        g.make_move()
        if g.is_game_over():
            g.declare_winner_loser()
            print("Das spiel wurde beendet, weil ein Spieler seine letzte Karte abgeworfen hat !")
        self.change_state(g)

    def change_state(self, g):
        g.set_state(NewTurnState())


class NewCardsState(GameState):

    def handle(self, g, data=None):
        print("*** CLASS: ", self, " ***")

        g.active_player.draw_card()
        g.active_player.draw_card()
        output = self.dc.gamelogic_to_net(g)
        # TODO / Nicht nötig: Die zwei neuen Karten printen
        self.change_state(g)
        return output

    def change_state(self, g):
        g.set_state(SecondAttemptState())


class SecondAttemptState(GameState):

    def handle(self, g, data=None):
        print("*** CLASS: ", self, " ***")

        print("Vom Client verschickte Dictionary: ", data)
        processed_data = self.dc.net_to_gamelogic(data, g)
        if g.is_game_over():
            return False
        cards = processed_data.get("selected_cards")
        print("Ausgewählte Karten:", cards)
        turn_valid = g.turns[-1].is_valid(cards)
        # TODO / Nicht nötig: Die aktualisierte Spielerhand printen
        if not turn_valid:
            g.disqualify_player(g.active_player, "Invalider Spielzug..")
            g.declare_winner_loser()
        print("Ist der Zug valide: ", turn_valid)
        self.change_state(g)
        print("*************")
        return turn_valid

    def change_state(self, g):
        g.set_state(FinishTurnState())