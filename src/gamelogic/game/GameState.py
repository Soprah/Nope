from src.dataconvert.DataConvert import DataConvert
from src.gamemanagement.GameManagement import GameManagement


class GameState:

    dc = DataConvert()
    gm = GameManagement.get_instance(self=GameManagement)

    def handle(self, g):
        pass

    def __str__(self):
        return type(self).__name__


class NewTurnState(GameState):

    def handle(self, g, data=None):
        print("Created a new turn object !")
        print("Sending the data to the client . . .")

        # Funktionen
        g.next_turn()
        g.state_output = self.dc.gamelogic_to_net(g)
        self.gm.send_turn_data(g.state_output, g.active_player)
        self.gm.send_turn_data(g.state_output)

    def change_state(self, g):
        g.set_state(FirstAttemptState())


class FirstAttemptState(GameState):

    def handle(self, g, data=None):
        print("The client does his first attempt !")
        print("Does he need another turn . . . ?")

        # Funktionen

    def change_state(self, g):
        '''
        if condition == 3:
            g.set_state(FinishTurnState())
        else:
            g.set_state(NewCardsState())
        '''


class FinishTurnState(GameState):

    def handle(self, g, data=None):
        print("No, he does not need another turn !")
        print("Finishing the turn. ")

    def change_state(self, g):
        g.set_state(NewTurnState())


class NewCardsState(GameState):

    def handle(self, g, data=None):
        print("The client draws two more cards and starts a second attempt !")
        print("Sending the data to the client . . .")

    def change_state(self, g):
        g.set_state(SecondAttemptState())


class SecondAttemptState(GameState):

    def handle(self, g, data=None):
        print()