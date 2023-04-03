class Family:
    def __init__(self) -> None:
        self.members_keys = ['name', 'age', 'gender', 'is_child']
        self.members = [
                    {'name':'Michael','age':35,'gender':'Male','is_child':False},
                    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
                    ]
        self.last_name = 'Someones'
    
    def born(self, **kwargs):
        new_member = dict(i for i in kwargs.items())
        if 'name' in new_member.keys():
            print(f"Congrats, {new_member['name']} is a new family member")
            self.members.append(new_member)
            print(self.members)
        else:
            print("Couldn't find a person")

    def is_18(self, name):
        return ([i['age'] for i in self.members if i['name'] == name][0] > 18)
    
    def family_presentation(self):
        print(f"{self.last_name} consist of:")
        for i in self.members:
            print(i['name'])
            

fam = Family()
fam.born(name = 'Someone', age = 19, gender = 'Male')
print(fam.is_18('Someone'))
fam.family_presentation()


class TheIncredibles(Family):
    
    def __init__(self) -> None:
        super().__init__()
        self.members = [
                        {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'MikeFly'},
                        {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'SuperWoman'}
                        ]
        
    def use_power(self, name):
        if self.is_18(name):
            print ([i['power'] for i in self.members if i['name'] == name][0])
        
        
    def family_presentation(self):
        super().family_presentation()
        print(f"Member's of {self.last_name}: ")
        for i in self.members:
            print(f"{i['name']} can {i['power']}" )


fam_2=TheIncredibles()
fam_2.family_presentation()