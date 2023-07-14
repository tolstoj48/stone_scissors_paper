# dokumentovat a dokomentovat celou hru dle: https://realpython.com/documenting-python-code/
# napsat si k tomu testy

import random
import sys


class Game:
    """A class to represent the Stone, scissors, paper game.

    Attributes
    ----------
    player_1 : instance of Player class
        the first instance of Player class - player that plays
    player_2 : instance of Player Class
        the second instance of Player class - player that plays
    num_of_wins : int
        the number of wins to play to (default False)

    Methods
    -------
    play()
        Runs and assess the whole state of the game
    """

    def __init__(self, player_1, player_2, num_of_wins=False):
        """
        Parameters
        ----------
        player_1 : instance of Player class
            the first instance of Player class - player that plays
        player_2 : instance of Player Class
            the second instance of Player class - player that plays
        num_of_wins : int
            the number of wins to play to (default False)
        """

        self.player_1 = player_1
        self.player_2 = player_2
        if int(num_of_wins):
            self.num_of_wins = int(num_of_wins)
        else:
            self.num_of_wins = self.__fetch_num_of_wins()
        self.score = [0, 0]

    def play(self):
        if self.num_of_wins == 0:
            print("Number of wins must be higher then 0.")
        while self.score[0] < self.num_of_wins or self.score[1] < self.num_of_wins:
            roll_1 = self.player_1.roll()
            roll_2 = self.player_2.roll()
            if roll_1 == 1 and roll_2 == 2:
                self.score[0] += 1
            elif roll_1 == 2 and roll_2 == 3:
                self.score[0] += 1
            elif roll_1 == 3 and roll_2 == 1:
                self.score[0] += 1
            elif roll_1 == 3 and roll_2 == 2:
                self.score[1] += 1
            elif roll_1 == 2 and roll_2 == 1:
                self.score[1] += 1
            elif roll_1 == 1 and roll_2 == 3:
                self.score[1] += 1
            state = self.__evaluate()
            if state:
                self.__print_result()
                break

    def __fetch_num_of_wins(self):
        num_of_wins = False
        while not num_of_wins:
            try:
                num_of_wins = input(
                    "Please, choose number of wins you want to play to. Must be between 1 and 10:")
                if int(num_of_wins) > 10 or int(num_of_wins) < 1:
                    print("Fetch me number between 1 and 10, please.")
                    num_of_wins = False
            except ValueError:
                print("Fetch me a valid number between 1 and 10, please.")
                num_of_wins = False
        return int(num_of_wins)

    def __evaluate(self):
        self.__show_score()
        if self.score[0] == self.num_of_wins or self.score[1] == self.num_of_wins:
            return True

    def __show_score(self):
        print('--------------------------------------------')
        print(
            f'The score is {self.player_1.name}: {self.score[0]} and {self.player_2.name}: {self.score[1]}!')
        print('--------------------------------------------')
        return

    def __print_result(self):
        if self.score[0] > self.score[1]:
            print(f'And the winner is {self.player_1.name}!!!')
        else:
            print(f'And the winner is {self.player_2.name}!!!')
        return


class Player:
    def __init__(self, name):
        self.name = name
        self.possible_results = {"1": "scissors", "2": "paper", "3": "stone"}

    def roll(self):
        return


class PlayerHuman(Player):
    def __init__(self, name=None):
        if name:
            self.name = name
        else:
            self.name = self.choose_name()
        super().__init__(self.name)

    def roll(self):
        roll = False
        while not roll:
            print('--------------------------------------------')
            print(
                f'Please give me 1 for {self.possible_results["1"]}, 2 for {self.possible_results["2"]}, 3 for {self.possible_results["3"]}')
            roll = input("What is your choice?")
            print('--------------------------------------------')
            if roll not in ["1", "2", "3"]:
                roll = False
                print(f'Give me, please, a valid input - 1, 2 or 3.')
        print(f'You rolled: {self.possible_results[roll]}')
        return int(roll)

    def choose_name(self):
        name = input("Please, choose your name:")
        if name:
            return name
        return "Anonymous"


class PlayerPc(Player):
    def __init__(self, name="Computer"):
        super().__init__(name)

    def roll(self):
        roll = random.randint(1, 3)
        print(f"{self.name} rolled: {self.possible_results[str(roll)]}")
        return roll


if __name__ == "__main__":
    # if there is more then three arguments from cmd line - suppose a try to hack :-)
    if len(sys.argv) > 3:
        print("You are supposed to provide max. two arguments - first is your name, second is the number of wins to play to.")
    # if there is name and number from cmd line - suppose user wants to play against computer
    if len(sys.argv) == 3:
        player_1 = PlayerHuman(sys.argv[1])
        player_2 = PlayerPc()
        game = Game(player_1, player_2, sys.argv[2])
        game.play()
    # if there is only number of wins to play to from cmd line - play default game computer vs. computer
    elif len(sys.argv) == 2:
        player_1 = PlayerPc()
        player_2 = PlayerPc()
        game = Game(player_1, player_2)
        game.play()
    # if there is no argument from cmd line - play default game computer vs. player
    elif len(sys.argv) == 1:
        player_1 = PlayerHuman()
        player_2 = PlayerPc()
        game = Game(player_1, player_2)
        game.play()
