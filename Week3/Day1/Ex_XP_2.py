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