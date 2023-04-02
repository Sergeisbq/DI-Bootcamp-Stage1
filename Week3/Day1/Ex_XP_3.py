class Song:

    def __init__(self, lyrics: list):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for i in self.lyrics:
            print(i)
            
stairway = ["There's a lady who's sure","all that glitters is gold", "and she's buying a stairway to heaven"] 

Song(stairway).sing_me_a_song()


###

class Zoo:
    def __init__(self, name) -> None:
          self.name=name
          self.animals=[]
          
    def add_animal(self, animal):
        if not animal in self.animals:
              self.animals.append(animal)
              
    def get_animals(self):
        print(self.animals)
        
    def sell_animal(self, animal):
        if animal in self.animals:
              self.animals.pop(self.animals.index(animal))
        
    def sort_animals(self):
        self.sort_animals=[[]]
        self.animals.sort()
        let=0
        for i,p in enumerate(self.animals):
            if p[0]!= self.animals[(i-1) if i>0 else 0][0]:
                let+=1
                self.sort_animals.append([])
            self.sort_animals[let].append(p)
        print (self.sort_animals)
        
    def get_groups(self):
        print("group:")
        list(map(print, self.sort_animals))
            

    
new_zoo=Zoo("Moscow")
new_zoo.add_animal("Baboon")
new_zoo.add_animal("Cougar")
new_zoo.add_animal("Cat")
new_zoo.add_animal("Bear")
new_zoo.add_animal("Ape")
new_zoo.add_animal("Emu")
new_zoo.add_animal("Eel")
new_zoo.add_animal("Giraffe")

new_zoo.get_animals()
new_zoo.sell_animal("Ape")
new_zoo.get_animals()
new_zoo.sort_animals()
new_zoo.get_groups()