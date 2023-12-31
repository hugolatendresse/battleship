import random
import numpy as np
from src.field import Field

# TODO separate the strategy from the skeleton of player, and implement a reinforcement learning AI in pick. Something like this:
# def pick(self):
#     if np.random.rand() < self.epsilon:  # Explore: choose a random action
#         return self.choose_random()
#     else:  # Exploit: choose the action with max Q-value
#         state = self.screen.arr.flatten()
#         action = np.argmax(self.q_table[state])
#         return np.unravel_index(action, self.screen.arr.shape)


class Player:
    def __init__(self, other_play_arr=None):
        self.other_play_secret_arr=other_play_arr
        self.board = Field()
        self.board.add_all_boats()
        self.screen = Field()
        self.screen.arr -= 1
        self.shots_fired = 0
        self.new_row = None
        self.new_col = None
        self.create_available_spots()
        self.available_spots = [(i,j) for i in range(10) for j in range(10)]

    def create_available_spots(self):
        spots1 = [(i, i) for i in range(1,9)]
        random.shuffle(spots1)
        spots2 = [(9-i, i) for i in range(1,9)]
        random.shuffle(spots2)
        self.available_spots = spots1 + spots2
        spots3 = list(set([(i,j) for i in range(10) for j in range(10)]) - set(self.available_spots))
        random.shuffle(spots3)
        self.available_spots += spots3
        assert len(self.available_spots)==100

    @property
    def reward(self):
        return self.screen.arr.sum() - self.shots_fired

    def choose_random(self):
        self.new_row, self.new_col = self.available_spots.pop(0)
        pass
        while (self.screen.arr[self.new_row, self.new_col] != -1) | (not self.is_no_neighboor_sunk) | (not self.is_all_diagonals_empty):
            if self.other_play_secret_arr[self.new_row, self.new_col]>0:
                pass
            self.new_row, self.new_col = self.available_spots.pop(0)
            pass
        return self.new_row, self.new_col

    @property
    def is_all_diagonals_empty(self):
        return (self.up_left in [-1, 0]) & \
               (self.up_right in [-1, 0]) & \
               (self.down_right in [-1, 0]) & \
               (self.down_left in [-1, 0])

    @property
    def is_no_neighboor_sunk(self):
        return (self.up in [-1, 0, 10]) & \
               (self.left in [-1, 0, 10]) & \
               (self.down in [-1, 0, 10]) & \
               (self.right in [-1, 0, 10])

    def pick(self):
        if self.shots_fired < 10:
            return self.try_returning(self.shots_fired, self.shots_fired)
        elif self.shots_fired<20:
            new_row = 19-self.shots_fired
            new_col = self.shots_fired-10
            return self.try_returning(new_row, new_col)
        elif (self.screen.arr==10).sum()>0:
            return self.finish_a_boat()
        else:
            return self.choose_random()

    def try_returning(self, row, col):
        if self.screen.arr[row, col] == -1:
            return row, col
        else:
            return self.choose_random()

    @property
    def up(self):
        return self.screen.access(self.new_row-1, self.new_col)

    @property
    def down(self):
        return self.screen.access(self.new_row+1, self.new_col)

    @property
    def left(self):
        return self.screen.access(self.new_row, self.new_col-1)

    @property
    def right(self):
        return self.screen.access(self.new_row, self.new_col+1)

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

    @property
    def up_right(self):
        return self.screen.access(self.new_row-1, self.new_col+1)

    @property
    def down_right(self):
        return self.screen.access(self.new_row+1, self.new_col+1)

    @property
    def up_left(self):
        return self.screen.access(self.new_row-1, self.new_col-1)

    @property
    def down_left(self):
        return self.screen.access(self.new_row+1, self.new_col-1)
