import numpy as np


def create_field():
    return np.zeros((10, 10))


def create_boats():
    return [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]


def add_fields(field1, field2):
    return field1 + field2


def sum_field(field):
    return field.sum()


def max_field(field):
    return field.max()


def getRandomInt(max):
    return np.random.randint(max)


def add_boat(field, boat_length):
    boat_field = create_field()
    row = getRandomInt(10)
    col = getRandomInt(10)
    direction = getRandomInt(2)
    if direction == 0:
        if row + boat_length > 9:
            return add_boat(field, boat_length)
        else:
            for inc_row in range(boat_length):
                boat_field[row + inc_row][col] = 5
    else:
        if col + boat_length > 9:
            return add_boat(field, boat_length)
        else:
            for inc_col in range(boat_length):
                boat_field[row][col + inc_col] = 5
    out = add_fields(boat_field, field)
    if out.max() == 5:
        # TODO cant allow two boats to touch either, even diagonally
        return out
    else:
        return add_boat(field, boat_length)


def add_all_boats(field, boats):
    for boat in boats:
        field = add_boat(field=field, boat_length=boat)


field1 = create_field()
field2 = create_field()
boats1 = create_boats()
boats2 = create_boats()
field1 = add_all_boats(field1, boats1)
field2 = add_all_boats(field2, boats2)
pass
# TODO: can't allow two boats to touch, even diagonally
