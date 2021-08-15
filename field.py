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
            test = col + boat_length
            if test > 9:
                return self.add_boat(boat_length=boat_length)
            else:
                boat_field.add_across(row=row, col=col, boat_length=boat_length)
        else:
            test = row + boat_length
            if test > 9:
                return self.add_boat(boat_length=boat_length)
            else:
                boat_field.add_down(row=row, col=col, boat_length=boat_length)
        assert boat_field.arr.sum() > 0
        boat_field.arr2 = np.where(boat_field.arr == boat_length / 2, 0, boat_field.arr)
        if (self.arr * boat_field.arr).sum() == 0:
            assert(np.count_nonzero(boat_field.arr2==boat_length)==boat_length)
            self.arr += boat_field.arr2
            return
        else:
            return self.add_boat(boat_length)
