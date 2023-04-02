class Zoo:

    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        if animal not in self.animals:
            self.animals.append(animal)

    def get_animals(self):
        print(self.animals)

    def sell_animal(self, animal):
        if animal in self.animals:
            self.animals.pop(self.animals.index(animal))

    def sort_animals(self):
        self.sort_animals = [[]]
        self.sort_animals.sort()
        a = 1
        for i, p in enumerate(self.animals):
            if p[0]

Zoo.add_animal('cow', 5)