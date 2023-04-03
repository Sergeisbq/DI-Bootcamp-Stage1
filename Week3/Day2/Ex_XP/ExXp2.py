# 2
class Dogs:

    def __init__(self, name, age: int, weight: int):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return (f'{self.name} is barking')

    def run_speed(self):
        return (self.weight / self.age) * 10
    
    def fight(self, other_dog):

        if self.run_speed() * self.weight > other_dog.run_speed() * other_dog.weight:
            return (f'{self.name} is a winner his power is {self.run_speed() * self.weight}')
        else:
            return (f'{other_dog.name} is a winner his power is {other_dog.run_speed() * other_dog.weight}')


if __name__ == '__main__':
    my_dogs = [Dogs('Barkley', 12, 40), Dogs('Rex', 8, 45), Dogs('Mailo', 4, 20)]
    print(my_dogs[0].fight(my_dogs[1]))
    # print(my_dogs[1].fight(my_dogs[2]))
    # print(my_dogs[2].fight(my_dogs[0]))



    
    