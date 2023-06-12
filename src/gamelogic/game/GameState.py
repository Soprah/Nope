import random


class GameState:

    def handle(self, g):
        pass

    def __str__(self):
        return type(self).__name__


class SetUpState(GameState):

    def handle(self, g):
        print("Executed all functions to prepare a game !")
        print("Ready to start!")
        g.set_value(1)

    def change_state(self, g):
        g.set_state(NewTurnState())


class NewTurnState(GameState):

    def handle(self, g):
        print("Created a new turn object !")
        print("Sending the data to the client . . .")
        g.set_value(2)

    def change_state(self, g):
        g.set_state(FirstAttemptState())


class FirstAttemptState(GameState):

    def handle(self, g):
        print("The client does his first attempt !")
        print("Does he need another turn . . . ?")
        zahl = random.randint(3, 4)
        g.set_value(zahl)

    def change_state(self, g):
        condition = g.get_value()
        if condition == 3:
            g.set_state(FinishTurnState())
        else:
            g.set_state(NewCardsState())


class FinishTurnState(GameState):

    def handle(self, g):
        print("No, he does not need another turn !")
        print("Finishing the turn. ")

    def change_state(self, g):
        g.set_state(NewTurnState())


class NewCardsState(GameState):

    def handle(self, g):
        print("The client draws two more cards and starts a second attempt !")
        print("Sending the data to the client . . .")

    def change_state(self, g):
        g.set_state(SecondAttemptState())


class SecondAttemptState(GameState):

    def handle(self, g):
        print()


class Game:

    def __init__(self):
        self.value = 0
        self.state = SetUpState()

    def execute(self):
        self.state.handle(self)

    def change_state(self):
        self.state.change_state(self)

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value


game = Game()

# Zustand 1
print("State: ", game.get_state())
game.execute()
print("Value: ", game.get_value())
game.change_state()

# Zustand 2
print("State: ", game.get_state())
game.execute()
print("Value: ", game.get_value())
game.change_state()

# Zustand 3
print("State: ", game.get_state())
game.execute()
print("Value: ", game.get_value())
game.change_state()

# Zustand 4
print("State: ", game.get_state())
game.execute()
print("Value: ", game.get_value())

