class Zoo:

    def __init__ (self, name) -> None:
        self.name = name
        self.animals = []

    def add_animal(self, new_animal: str):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animal(self) -> None:
        print(self.animals)

    def sell_animal(self, animal_sold: str) -> None:
        self.animals.remove(animal_sold)

    def sort_animals(self) -> dict:
        animals_sorted_list = sorted(self.animals)
        animals_sorted_dict = {}
        index = 1
        for animal in animals_sorted_list:
            if index not in animals_sorted_dict:
                animals_sorted_dict[index] = animal
            else:
                if isinstance(animals_sorted_dict[index], str):
                    if animals_sorted_dict[index][0] == animal[0]:
                        animal_list = []
                        animal_list.append(animals_sorted_dict[index])
                        animal_list.append(animal)
                        animals_sorted_dict[index] = animal_list
                    else:
                        index += 1
                        animals_sorted_dict[index] = animal
                elif isinstance(animals_sorted_dict[index], list):
                    if animals_sorted_dict[index][0][0] == animal[0]:
                        animals_sorted_dict[index].append(animal)
        return animals_sorted_dict

zoo = Zoo('Ramat_gan')
zoo.add_animal('Ape')
zoo.add_animal('Baboon')
zoo.add_animal('Bear')
zoo.add_animal('Cat')
zoo.add_animal('Cougar')
zoo.add_animal('Eel')
zoo.add_animal('Emu')
print(Zoo.sort_animals())

