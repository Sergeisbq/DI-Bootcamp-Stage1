#1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict_i = dict(zip(keys, values))
print(dict_i)


#2
family_member_names = []
family_member_list = []

while True:
    family_member_names=input('Type your name (when finish, type quit): ')
    family_member_list.append(family_member_names)
    if family_member_names == 'quit':
        break

del family_member_list[-1]

print(family_member_list)

family_member_ages = []
family_member_ages_list = []

for i in family_member_list:
    if len(family_member_list) == len(family_member_ages_list):
        break
    else:
        family_member_ages = input(f'{i}, type your age (when finish, type 0): ')
        family_member_ages_list.append(family_member_ages)

print(family_member_ages_list)

dict_i = dict(zip(family_member_list, family_member_ages_list))
print(dict_i)

counter = 0

for value in dict_i.values():
    age = int(value)
    if age >= 12:
        counter += 15
    elif 3 <= age < 12:
        counter += 10
    else:
        counter += 0

print(counter)


#3
brand = {
        'name': 'Zara',
        'creation_date': 1975,
        'creator_name': 'Amancio Ortega Gaona',
        'type_of_clothes': ['men', 'women', 'children', 'home'],
        'international_competitors': ['Gap', 'H&M', 'Benetton'],
        'number_stores': 7000,
        'major_color': { 
                        'France': 'blue', 
                        'Spain': 'red', 
                        'US': ['pink', 'green']
                        }
        }

brand['number_stores'] = 2

client_1 = list(brand['type_of_clothes'])
clients_1 = client_1[0]
clients_2 = client_1[1]
clients_3 = client_1[2]
print(f'{clients_1}, {clients_2} and {clients_3} are clents of Zara')

brand['country_creation'] = 'Spain'

print(brand.get('international_competitors', 'None'))
brand.update ({'international_competitors': ['Gap', 'H&M', 'Benetton', 'Desigual']})
print(brand.get('international_competitors', 'None'))

brand.pop('creation_date')

print(brand['international_competitors'][-1])

print(brand['major_color']['US'])

print(len(brand))

for key in brand:
        print(key)

more_on_zara = {
        'name': 'Zara',
        'creation_date': 1975,
        'creator_name': 'Amancio Ortega Gaona',
        'type_of_clothes': ['men', 'women', 'children', 'home'],
        'international_competitors': ['Gap', 'H&M', 'Benetton'],
        'number_stores': 10000,
        'major_color': { 
                        'France': 'blue', 
                        'Spain': 'red', 
                        'US': ['pink', 'green']
                        }
        }

brand.update(more_on_zara)
print(brand['number_stores'])


#4
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
dict_d = {}
for i, char in enumerate(users):
     dict_d[char] = i
print(dict_d)

new_dict = {}
for i, char in dict_d.items():
    new_dict[char] = i
print(new_dict)

another_dict = {}
new_users = sorted(users)
for i, char in enumerate(new_users):
     another_dict[char] = i
print(another_dict)

newone_dict = []
for name in users:
     if 'i' in name:
        newone_dict.append(name)
print(newone_dict)

newone_dict_1 = []
for name in users:
     if 'M' in name[0]:
        newone_dict_1.append(name)
     elif 'P' in name[0]:
        newone_dict_1.append(name)
print(newone_dict_1)



