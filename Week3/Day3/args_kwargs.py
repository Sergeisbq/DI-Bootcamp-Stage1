class Family:

    def __init__(self, last_name: str, members: list[dict]) -> None:
        self.last_name = last_name
        self.members = members

    def born(self, **info):
        self.members.append(info)
        name = info['name']
        print(f"Congratulations for {name}!")

family_name = "Azi"
members = [
            {'name':'Michael','age':35,'gender':'Male','is_child':False},
            {'name':'Sarah','age':32,'gender':'Female','is_child':False}
            ]

azi_family = Family(family_name, members)
ben = {'name' : "Ben", 'age' : 0, 'gender' : "male", 'is_child' : True}
azi_family.born(**ben)
print(azi_family.members)