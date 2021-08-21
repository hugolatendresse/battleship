from Player import Player
from get_random_int import get_random_int


class Game:
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.print_all()

    def print_all(self):
        print("\nPlayer1: ")
        print(self.player1.screen.arr)
        print(self.player1.board.arr)
        print("\nPlayer2: ")
        print(self.player2.screen.arr)
        print(self.player2.board.arr)
        print('\n\n')

    def play(self):
        for i in range(50):
            self.player1_fires_random_at_player2()
            self.player2_fires_random_at_player1()
            pass
        pass

    def player1_fires_random_at_player2(self):
        self.shooter = self.player1
        self.shootee = self.player2
        self.fire_random()

    def player2_fires_random_at_player1(self):
        self.shooter = self.player2
        self.shootee = self.player1
        self.fire_random()

    def fire_random(self):
        self.row = get_random_int(10)
        self.col = get_random_int(10)
        self.try_again_if_was_already_tried()
        self.post_fire()

    def try_again_if_was_already_tried(self):
        if self.shooter.screen.arr[self.row, self.col] != -1:
            return self.fire_random()

    @property
    def result(self):
        return self.shootee.board.arr[self.row, self.col]

    def post_fire(self):
        print("player 1 fired at ({}, {})".format(self.row, self.col))
        print("this was a {} on player 2's board".format({self.result}))
        self.add_result_on_shooters_screen()
        self.print_all()

    def add_result_on_shooters_screen(self):
        if self.result == 0:
            self.shooter.screen.arr[self.row, self.col] = 0
        else:
            self.shooter.screen.arr[self.row, self.col] = 10
        # TODO shootee needs to tell shooter if boat is destroyed
