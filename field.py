import numpy as np
from get_random_int import get_random_int
from boat_field import NewBoatField

class Field:
    def __init__(self):
        self.arr = np.zeros((10, 10))

    def add_all_boats(self):
        for boat in self.boats:
            self.add_boat(boat_length=boat)

    @property
    def boats(self):
        return [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

    def add_boat(self, boat_length):
        boat_field = NewBoatField()
        row = get_random_int(10)
        col = get_random_int(10)
        direction = get_random_int(2)
        if direction == 0:
            if row + boat_length > 9:
                self.add_boat(boat_length)
            else:
                boat_field.add_across(row, col, boat_length)
        else:
            if col + boat_length > 9:
                self.add_boat(boat_length)
            else:
                boat_field.add_down(row, col, boat_length)
        if (boat_field.arr + self.arr).max() == 5:
            self.arr += boat_field.arr
        else:
            return self.add_boat(boat_length)


