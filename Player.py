from field import Field
from get_random_int import get_random_int


class Player:
    def __init__(self):
        self.board = Field()
        self.board.add_all_boats()
        self.screen = Field()
        self.screen.arr -= 1
        self.shots_fired = 0
        self.random_row = None
        self.random_col = None

    @property
    def reward(self):
        return self.screen.arr.sum() - self.shots_fired

    def choose_random(self):
        self.select_random_row_and_col()
        while self.screen.arr[self.random_row, self.random_col] != -1:
            self.select_random_row_and_col()
        return self.random_row, self.random_col

    def select_random_row_and_col(self):
        self.random_row = get_random_int(10)
        self.random_col = get_random_int(10)

    def pick(self):
        return self.choose_random() # TODO can do better!
