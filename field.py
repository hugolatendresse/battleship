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
        print("check a")
        boat_field = NewBoatField()
        row = get_random_int(10)
        col = get_random_int(10)
        direction = get_random_int(2)
        if direction == 0:
            test = col + boat_length
            if test > 9:
                print("check b")
                return self.add_boat(boat_length=boat_length)
                print("check c")
            else:
                print("check d")
                boat_field.add_across(row=row, col=col, boat_length=boat_length)
                print("check e")
        else:
            test = row + boat_length
            if test > 9:
                print("check f")
                return self.add_boat(boat_length=boat_length)
                print("check g")
            else:
                print("check h")
                boat_field.add_down(row=row, col=col, boat_length=boat_length)
                print("check i")
        if boat_field.arr.sum()==0:
            raise Exception
        boat_field.arr2 = np.where(boat_field.arr == boat_length / 2, 0, boat_field.arr)
        print("check j")
        if (self.arr * boat_field.arr).sum() == 0:
            print("existing sea:\n")
            print(self.arr)
            print("new boat\n")
            print(boat_field.arr2)
            if np.count_nonzero(boat_field.arr2==boat_length)!=boat_length:
                return self.add_boat(boat_length)
            self.arr += boat_field.arr2
            return
            print("check k")
        else:
            print("check l")
            return self.add_boat(boat_length)
            print("check m")
