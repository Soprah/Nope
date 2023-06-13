# from src.dataconvert.DataConvert import DataConvert
# from src.gamemanagement.GameManagement import GameManagement


class GameState:

    # dc = DataConvert()
    # gm = GameManagement.get_instance(self=GameManagement)

    def handle(self, g):
        pass

    def __str__(self):
        return type(self).__name__

    def __repr__(self):
        return type(self).__name__


class NewTurnState(GameState):

    def handle(self, g, data=None):
        if g.is_game_over() == False:
            print("Created a new turn object !")
            print("Sending the data to the client . . .")
            from src.dataconvert.DataConvert import DataConvert
            from src.gamemanagement.GameManagement import GameManagement
            # Objekte
            dc = DataConvert()
            gm = GameManagement.get_instance(self=GameManagement)

            # Funktionen
            g.next_turn()
            output = dc.gamelogic_to_net(g)
            # TODO: Folgende Methode entklammern
            # gm.send_turn_data(output, g.active_player)
            self.change_state(g)
            return output
        else:
            print("Das Spiel wurde beendet")
            g.finish_game()

    def change_state(self, g):
        g.set_state(FirstAttemptState())

    def __str__(self):
        return type(self).__name__

    def __repr__(self):
        return type(self).__name__


class FirstAttemptState(GameState):

    def handle(self, g, data=None):

        if g.is_game_over() == False:
            print("The client does his first attempt !")
            print("Does he need another turn . . . ?")

            from src.dataconvert.DataConvert import DataConvert
            from src.gamemanagement.GameManagement import GameManagement
            # Objekte
            dc = DataConvert()
            gm = GameManagement.get_instance(self=GameManagement)

            # Funktionen
            print("Vom Client verschickte Dictionary: ", data)
            processed_data = dc.net_to_gamelogic(data, g)
            cards = processed_data.get("selected_cards")
            print("Ausgewählte Karten:", cards)
            turn_valid = g.turns[-1].is_valid(cards)
            print(turn_valid)
            self.change_state(g)

        else:
            print("Spiel ist beendet!")
            g.finish_game()

    def __str__(self):
        return type(self).__name__

    def __repr__(self):
        return type(self).__name__

    def change_state(self, g):
        another_attempt_necessary = g.turns[-1].is_another_attempt_necessary()
        print("Muss man noch einen Spielzug machen? Antwort: ",another_attempt_necessary)
        if another_attempt_necessary:
            g.set_state(FinishTurnState())
        else:
            g.set_state(NewCardsState())

class FinishTurnState(GameState):

    def handle(self, g, data=None):
        if g.is_game_over() == False:
            print("No, he does not need another turn !")
            print("Finishing the turn. ")
            g.make_move()
        else:
            print("Spiel ist beendet!")
            g.finish_game()

    def change_state(self, g):
        g.set_state(NewCardsState())


class NewCardsState(GameState):

    def handle(self, g, data=None):
        if g.is_game_over() == False:
            print("The client draws two more cards and starts a second attempt !")
            print("Sending the data to the client . . .")
            g.active_player.draw_card()
            g.active_player.draw_card()

            from src.dataconvert.DataConvert import DataConvert
            from src.gamemanagement.GameManagement import GameManagement
            # Objekte
            dc = DataConvert()
            output = dc.gamelogic_to_net(g)
            # gm = GameManagement.get_instance(self=GameManagement)
            return output
        else:
            print("Spiel ist beendet!")
            g.finish_game()
    def change_state(self, g):
        g.set_state(SecondAttemptState())


class SecondAttemptState(GameState):

    def handle(self, g, data=None):
        if g.is_game_over() == False:
            print("Is the second attempt of the client valid ?")

            from src.dataconvert.DataConvert import DataConvert
            from src.gamemanagement.GameManagement import GameManagement
            # Objekte
            dc = DataConvert()
            output = dc.gamelogic_to_net(g)
            # gm = GameManagement.get_instance(self=GameManagement)
            return output
        else:
            print("Spiel ist beendet!")
            g.finish_game()
    def change_state(self, g):
        g.set_state(FinishTurnState())