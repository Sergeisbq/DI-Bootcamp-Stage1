import random

class Game():
    def __init__(self) -> None:
        pass


    def get_user_item(self):
        choice_u = ''
        while choice_u not in ['r', 'p', 's']:
            choice_u = input("Select (r)ock (p)aper (s)cissors: ")
        return choice_u
    

    def get_computer_item(self):
        list_1 = ['r', 'p', 's']
        return random.choice(list_1)
    

    def get_game_result(self, user_item, computer_item):
        a = user_item + computer_item
        if user_item == computer_item:
            return 'draw'
        else:
            if a == 'rp' or a == 'sr' or a == 'ps':
                return 'loss'
            else:
                return 'win'


    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        print(f"You selected {user_item}. The computer selected {computer_item}. The result is {result}")
        return result

        
            

