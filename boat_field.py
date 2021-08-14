import numpy as np
from get_random_int import get_random_int

class NewBoatField:
    def __init__(self):
        self.arr = np.zeros((10, 10))

    def add_across(self,row, col, boat_length):
        for rowright in range(row, row+boat_length):
            self.arr[rowright][col] = 5
        for rowright in range(row, row+boat_length):
            self.add_around(row=rowright, col=col)

    def add_down(self,row, col, boat_length):
        for coldown in range(col, col+boat_length):
            self.add_around(row=row, col=coldown)
        for coldown in range(col, col+boat_length):
            self.arr[row][coldown] = 5

    def add_boat_and_around(self, row, col):
        self.add_one_boat_spot(row=row, col=col)

    def add_one_boat_spot(self, row, col):
        self.arr[row, col] = 5

    def add_around(self, row, col):
        for row_inc in [-1, 0, 1]:
            for col_inc in [-1, 0, 1]:
                if (col_inc != 0) | (row_inc != 0):
                    new_row = row + row_inc
                    new_col = col + col_inc
                    if (new_row >= 0) & (new_row <= 9) & (new_col >= 0) & (new_col <= 9):
                        self.arr[new_row, new_col] = 4
