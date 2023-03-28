nambers_1 = [num for num in range(11)]
nambers_2 = [num for num in range(11, 22)]

print(nambers_1)
print(nambers_2)

connected = dict(zip(nambers_1, nambers_2))
print(connected)


family_member_names = []
family_member_list = []

while True:
    family_member_names=input('Type your name (when finish, type quit): ')
    family_member_list.append(family_member_names)
    if family_member_names == 'quit':
        break
    
print(family_member_list)