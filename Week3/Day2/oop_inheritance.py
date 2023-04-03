class Animal: #parent

    def __init__(self, name: str):
        self.name = name

    def breathing(self):
        out = f"{self.name} breaths"
        print(out)

class Mammal(Animal): #child
    def __init__(self, name: str, lungs: int):
       super().__init__(name, lungs)
       print(type(self))
       self.name = name
       self.lungs = lungs

class SeaMammal(Mammal):

    def __init__(self, name: str, lungs: int):
        super().__init__(name, lungs)
        print(type(self))

    def hold_breath(self):
        out = f"{self.name} holds breath"
        print(out)
m = Mammal('m', 2)
dolphin = SeaMammal('dolphin', 2)


