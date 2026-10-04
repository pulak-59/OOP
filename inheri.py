class father:
    def __init__(self, name):
        self. name = name

    def son(self):
        print(f"{self.name} is her son")

class sister(father):
    def same(self):
        print(f"{self.name} is his brother")


parent = sister("polok")
parent.son()
parent.same()
