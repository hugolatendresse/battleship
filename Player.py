import numpy as np

from field import Field
from get_random_int import get_random_int


class Player:
    def __init__(self):
        self.board = Field()
        self.board.add_all_boats()
        self.screen = Field()
        self.screen.arr -= 1
        self.shots_fired = 0
        self.new_row = None
        self.new_col = None

    @property
    def reward(self):
        return self.screen.arr.sum() - self.shots_fired

    def choose_random(self):
        self.select_random_row_and_col()
        while (self.screen.arr[self.new_row, self.new_col] != -1) | (not self.is_all_diagonals_empty) | (not self.is_no_neighboor_sunk):
            self.select_random_row_and_col()
        return self.new_row, self.new_col

    def select_random_row_and_col(self):
        self.new_row = get_random_int(10)
        self.new_col = get_random_int(10)

    @property
    def is_all_diagonals_empty(self):
        return (self.screen.arr[self.new_row + 1, self.new_col + 1] in [-1, 0]) & \
               (self.screen.arr[self.new_row + 1, self.new_col - 1] in [-1, 0]) & \
               (self.screen.arr[self.new_row - 1, self.new_col + 1] in [-1, 0]) & \
               (self.screen.arr[self.new_row - 1, self.new_col - 1] in [-1, 0])

    @property
    def is_no_neighboor_sunk(self):
        return (self.up in [-1, 0, 10]) & \
               (self.left in [-1, 0, 10]) & \
               (self.down in [-1, 0, 10]) & \
               (self.right in [-1, 0, 10])

    def pick(self):
        if self.shots_fired < 10:
            return self.shots_fired, self.shots_fired
        elif self.shots_fired<20:
            if ((19-self.shots_fired) != (self.shots_fired-10)):
                return 19-self.shots_fired, self.shots_fired-10
            else:
                return self.choose_random()
        elif (self.screen.arr==10).sum()>0:
            return self.finish_a_boat()
        else:
            return self.choose_random() # TODO can do better!

    @property
    def up(self):
        try:
            return self.screen.arr[self.new_row + 1, self.new_col]
        except Exception:
            return 0

    @property
    def down(self):
        try:
            return self.screen.arr[self.new_row - 1, self.new_col]
        except Exception:
            return 0

    @property
    def left(self):
        try:
            return self.screen.arr[self.new_row, self.new_col-1]
        except Exception:
            return 0

    @property
    def right(self):
        try:
            return self.screen.arr[self.new_row, self.new_col+1]
        except Exception:
            return 0

    def finish_a_boat(self):
        for self.new_row, self.new_col in zip(*np.where(self.screen.arr==10)):
            if (self.up==10) & (self.down==10):
                return self.choose_random()
            elif (self.left==10) & (self.right==10):
                return self.choose_random()
            elif (self.up==10) & (self.down==-1):
                return self.new_row+1, self.new_col
            elif (self.up==-1) & (self.down==10):
                return self.new_row-1, self.new_col
            elif (self.left==10) & (self.right==-1):
                return self.new_row, self.new_col+1
            elif (self.left==-1) & (self.right==10):
                return self.new_row, self.new_col-1
            else:
                return self.choose_random()

