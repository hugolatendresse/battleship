

class Game:
    def __init__(self):
        from field import Field
        self.field1 = Field()
        self.field2 = Field()
        self.field1.add_all_boats()
        self.field2.add_all_boats()
        print("\n")
        print(self.field1.arr)
        print("\n")
        print(self.field2.arr)

    def play(self):
        pass # TODO