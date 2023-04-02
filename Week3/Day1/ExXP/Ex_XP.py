# 1

class Cat:

    cats = []

    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
        Cat.cats.append(self)

    # dunder - double underscore / magic metgods
    def __str__(self) -> str:
        return self.name

cat1 = Cat('Mizzy', 5)
cat2 = Cat('Patsy', 7)
cat3 = Cat('Sky', 3)

def oldest_cat(cat_list: list) -> Cat:
    
    oldest = cat_list[0]
    for cat in cat_list:
        if cat.age > oldest.age:
            oldest = cat
    
    return oldest

cats = Cat.cats
oldest = oldest_cat(cats)
print(oldest)


# 2

class Dog:

    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height
        print(f'{dog_name} is {dog_height} cm high')
        
    def bark(self):
        print(f'{self.name} goes woof!')

    def jump(self):
        x = self.height * 2
        print(f'{self.name} jumps {x} cm high!')
        
davids_dog = Dog("Rex", 50)
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)
sarahs_dog.bark()
sarahs_dog.jump()

if sarahs_dog.height > davids_dog.height:
    print(f'{sarahs_dog.name} is bigger than {davids_dog.name}')
elif sarahs_dog.height == davids_dog.height:
    print(f'Dogs have the same height')
else:
    print(f'{davids_dog.name} is bigger than {sarahs_dog.name}')


# 3

class Song:

    def __init__(self, lyrics: list):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for i in self.lyrics:
            print(i)
            
stairway = ["There's a lady who's sure","all that glitters is gold", "and she's buying a stairway to heaven"] 

Song(stairway).sing_me_a_song()


# 4

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