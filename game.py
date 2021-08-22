from copy import deepcopy

import numpy as np

from Player import Player
from get_random_int import get_random_int


class Game:
    def __init__(self, game_type="machine_vs_machine", verbose='yes'):
        """ game_type: machine_vs_machine or human_vs_human
            verbose: zero, little, or yes"""
        self.game_type = game_type
        self.player1 = Player()
        self.player2 = Player()
        self.turn = "player1"
        self.winner = ""
        self.verbose = verbose
        self.number_of_shots_to_win = None

    def print_all(self):
        print("\nPlayer1: ")
        print(self.player1.screen.arr)
        print(self.player1.board.arr)
        print("\nPlayer2: ")
        print(self.player2.screen.arr)
        print(self.player2.board.arr)
        print('\n\n')

    def play(self):
        if self.verbose == "little":
            self.print_all()
        while self.winner == "":
            self.turn = "player1"
            self.player_fires()
            self.turn = "player2"
            self.player_fires()
        if self.verbose == "little":
            self.print_all()
        self.declare_winner()
        return self.winner, self.number_of_shots_to_win

    def declare_winner(self):
        if self.verbose != "zero":
            print("{} has won in {} shots".format(self.winner, self.number_of_shots_to_win))

    @property
    def shooter(self):
        if self.turn=="player1":
            return self.player1
        elif self.turn=="player2":
            return self.player2
        else:
            raise Exception

    @property
    def shootee(self):
        if self.turn=="player1":
            return self.player2
        elif self.turn=="player2":
            return self.player1
        else:
            raise Exception

    def player_fires(self):
        if self.game_type == "machine_vs_machine":
            self.fire_random()
        else:
            choice = input("Where should {} fire? Input in XY format or press Enter to fire random".format(self.turn))
            if choice=="":
                self.fire_random()
            else:
                if len(choice)!=2:
                    print("The answer should have two characters (each one a digit)")
                    self.player_fires()
                try:
                    row=int(choice[0])
                    col=int(choice[1])
                except Exception:
                    print("The answer should have two characters (each one a digit)")
                    self.player_fires()
                if (row>9) or (row<0) or (col>9) or (col<0):
                    print("The answer should have two characters (each one a digit betweeen 0 and 9)")
                    self.player_fires()
                self.fire_selected(row=row, col=col)

    def fire_random(self):
        self.select_random_row_and_col()
        while self.shooter.screen.arr[self.row, self.col] != -1:
            self.select_random_row_and_col()
        self.post_fire()

    def select_random_row_and_col(self):
        self.row = get_random_int(10)
        self.col = get_random_int(10)

    def fire_selected(self, row, col):
        self.row = row
        self.col = col
        self.ask_for_new_if_it_was_already_tried()
        self.post_fire()

    def ask_for_new_if_it_was_already_tried(self):
        if self.shooter.screen.arr[self.row, self.col] != -1:
            "This location has already been shot at. Please try again."
            return self.player_fires()

    @property
    def result(self):
        return self.shootee.board.arr[self.row, self.col]

    def post_fire(self):
        if self.verbose=="yes":
            print("{} fired at ({}, {}) which hit a {}".format(self.turn, self.row, self.col, self.result))
        self.update_fields()
        if self.verbose=="yes":
            self.print_all()
        self.shooter.shots_fired += 1
        self.check_win()

    def update_fields(self):
        if self.result == 0:
            self.shooter.screen.arr[self.row, self.col] = 0
        else:
            self.shooter.screen.arr[self.row, self.col] = 10
            self.shootee.board.arr[self.row, self.col] = 10
            if self.boat_is_sank:
                self.sink_boat()

    def sink_boat(self):
        for self.row, self.col in zip(*np.where(self.shootee.board.arr==10)):
            if self.boat_is_sank:
                self.shootee.board.arr[self.row, self.col] = 15
                self.shooter.screen.arr[self.row, self.col] = 15

    @property
    def boat_is_sank(self):
        return (self.shootee.board.access(self.row - 1, self.col) in [0, 10, 15]) & \
               (self.shootee.board.access(self.row + 1, self.col) in [0, 10, 15]) & \
               (self.shootee.board.access(self.row, self.col - 1) in [0, 10, 15]) & \
               (self.shootee.board.access(self.row, self.col + 1) in [0, 10, 15])

    def check_win(self):
        for value in [1, 2, 3, 4]:
            if value in self.shootee.board.arr:
                return
        self.winner += deepcopy(self.turn)
        self.number_of_shots_to_win = self.shooter.shots_fired

"""
0: water
1-4: a boat part that wasnt hit
-1: unkowwn
10: a boat part that was hit but not sinked
15: a sinked boat
"""