class Player:
    
    def __init__(self, name, strength, speed, level = 0):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.level = level

    def jump(self):
        jump_height = (self.strength * self.speed) // 100
        print(f'{self.name} jumps {jump_height}!')

    def level_up(self):
        self.level_up += 1
        print(f'Leveled up to {self.level}')

# method - function from a class
# conan is an instance of class Players
conan = Player('Conan', 100, 55)
conan.jump()

conan.location = 'TLV'
# instance 
xena = Player('Xena', 80, 100, 3)
xena.jump()
