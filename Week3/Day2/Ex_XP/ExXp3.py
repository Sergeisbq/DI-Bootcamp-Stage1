# 3
import random

from ExXp2 import Dogs

class PetDog(Dogs):

    def __init__(self, name, age, weight, trained = False):
        super().__init__(name, age, weight)
        self.trained = trained
        
    def train(self):
        self.trained = True
        self.bark()
    
    def play(self, *args):
        my_dogs = [n.name for n in args]
        my_dogs.append(self.name)
        my_dogs=(', ').join(my_dogs)
        print(f'{my_dogs} all play together')

    def do_a_trick(self):
        if self.trained:
            tricks = ['does a barrel roll','stands on his back legs','shakes your hand','plays dead']
            trick = random.choice(tricks)
            print(f"{self.name} {trick}")
        
dog_1 = PetDog('Barkley', 12, 40)
dog_2 = PetDog('Rex', 8, 45)
dog_3 = PetDog('Mailo', 4, 20)
  
dog_1.do_a_trick()
dog_1.train()
dog_1.do_a_trick()
dog_1.play(dog_2,dog_3)





