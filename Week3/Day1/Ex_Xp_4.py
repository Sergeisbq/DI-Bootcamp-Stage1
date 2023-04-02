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
        a = 0
        for i, p in enumerate(self.animals):
            if p[0] != self.animals[(i - 1) if i != 0 else 0][0]:
                a += 1
                self.sort_animals.append([])
            self.sort_animals[a].append(p)
        print(self.sort_animals)

    def get_groups(self):
        list(map(print, self.sort_animals))

    def ramat_gan_safari(self):
        my_zoo.get_animals()
        my_zoo.sell_animal("Ape")
        my_zoo.get_animals()
        my_zoo.sort_animals()
        my_zoo.get_groups()

my_zoo=Zoo("ramatgan_zoo")
my_zoo.add_animal("Ape")
my_zoo.add_animal("Baboon")
my_zoo.add_animal("Bear")
my_zoo.add_animal("Cat")
my_zoo.add_animal("Cougar")
my_zoo.add_animal("Eel")
my_zoo.add_animal("Emu")
my_zoo.add_animal("Giraffe")

my_zoo.ramat_gan_safari()