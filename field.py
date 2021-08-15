import numpy as np
from get_random_int import get_random_int
from boat_field import NewBoatField

class Field:
    def __init__(self):
        self.arr = np.zeros((10, 10))
        self.cnt=0

    def add_all_boats(self):
        for boat in self.boats:
            self.add_boat(boat_length=boat)

    @property
    def boats(self):
        return [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

    def add_boat(self, boat_length):
        self.cnt+=1
        if self.cnt>99:
            pass
        boat_field = NewBoatField()
        row = get_random_int(10)
        col = get_random_int(10)
        direction = get_random_int(2)
        if direction == 0:
            test = col + boat_length
            if test > 9:
                self.add_boat(boat_length)
            else:
                boat_field.add_across(row, col, boat_length)
        else:
            test = row + boat_length
            if test > 9:
                self.add_boat(boat_length)
            else:
                boat_field.add_down(row, col, boat_length)
        if (boat_field.arr + self.arr).max() == 5:
            # print("existing sea:\n")
            # print(self.arr)
            # print("new boat\n")
            # print(boat_field.arr)
            boat_field.arr2 = np.where(boat_field.arr == 4, 0, boat_field.arr)
            if np.count_nonzero(boat_field.arr2==5)!=boat_length:
                self.add_boat(boat_length)
            self.arr += boat_field.arr2
        else:
            self.add_boat(boat_length)
