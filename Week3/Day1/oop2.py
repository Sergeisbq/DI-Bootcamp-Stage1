class Human:

    population = 0
    instances = []

    def __init__(self, first_name, last_name = 'Smith') -> None:
        self.first_name = first_name
        self.last_name = last_name

        self.fullname = self.first_name + ' ' + self.last_name
        Human.population += 1
        Human.instances.append(self)

h1 = Human('A')
h2 = Human('B')
h3 = Human('D')
h4 = Human('D')

print(Human.population)

print(h1.fullname)
print(Human.instances)

