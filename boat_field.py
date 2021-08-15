import numpy as np
from get_random_int import get_random_int

class NewBoatField:
    def __init__(self):
        self.arr = np.zeros((10, 10))
        self.arr2 = None

    def add_across(self,row, col, boat_length):
        for colright in range(col, col+boat_length):
            self.add_around(row=row, col=colright, boat_length=boat_length)
        for colright in range(col, col+boat_length):
            self.arr[row][colright] = boat_length
        if self.arr.sum()==0:
            raise Exception

    def add_down(self,row, col, boat_length):
        for rowdown in range(row, row+boat_length):
            self.add_around(row=rowdown, col=col, boat_length=boat_length)
        for rowdown in range(row, row+boat_length):
            self.arr[rowdown][col] = boat_length
        if self.arr.sum()==0:
            raise Exception

    def add_around(self, row, col, boat_length):
        for row_inc in [-1, 0, 1]:
            for col_inc in [-1, 0, 1]:
                if (col_inc != 0) | (row_inc != 0):
                    new_row = row + row_inc
                    new_col = col + col_inc
                    if (new_row >= 0) & (new_row <= 9) & (new_col >= 0) & (new_col <= 9):
                        self.arr[new_row, new_col] = boat_length/2
