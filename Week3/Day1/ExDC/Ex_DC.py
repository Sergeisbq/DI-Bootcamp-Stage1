class Farm:

    animals = {}
    animal_types = []

    def __init__(self, farm_name):
        self.farm_name = farm_name
        self.animals = {}
        self.animal_types = []
        

    def add_animal(self, animal, amount = 1):
        if animal not in self.animals.keys():
            self.animals[animal] = amount
        else:
            self.animals[animal] += amount

    def get_animal_types(self):
        return sorted(list(self.animals.keys()))
    
    def get_short_info(self):
        r=self.get_animal_types()
        return (f"McDonald's farm has {r[0]}s, {r[1]}s and {r[2]}")
    
    def get_main_text(self):
        r=self.get_animal_types()
        return (f'''McDonald's farm:
{r[0]}  :  5
{r[1]}  :  2
{r[2]}  :  12

    E-I-E-I-0!
    ''')
        

mcdonald = Farm("McDonald")

mcdonald.add_animal('cow',5)
mcdonald.add_animal('sheep')
mcdonald.add_animal('sheep')
mcdonald.add_animal('goat', 12)
# print(macdonald.get_info())
print(mcdonald.get_main_text())
print(mcdonald.get_animal_types())
print(mcdonald.get_short_info())

