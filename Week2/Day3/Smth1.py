# brand = {
#         'name': 'Zara',
#         'creation_date': 1975,
#         'creator_name': 'Amancio Ortega Gaona',
#         'type_of_clothes': ['men', 'women', 'children', 'home'],
#         'international_competitors': ['Gap', 'H&M', 'Benetton'],
#         'number_stores': 7000,
#         'major_color': { 
#                         'France': 'blue', 
#                         'Spain': 'red', 
#                         'US': ['pink', 'green']
#                         }
#         }

# brand['number_stores'] = 2

# client_1 = list(brand['type_of_clothes'])
# clients_1 = client_1[0]
# clients_2 = client_1[1]
# clients_3 = client_1[2]
# print(f'{clients_1}, {clients_2} and {clients_3} are clents of Zara')

# brand['country_creation'] = 'Spain'

# print(brand.get('international_competitors', 'None'))
# brand.update ({'international_competitors': ['Gap', 'H&M', 'Benetton', 'Desigual']})
# print(brand.get('international_competitors', 'None'))

# brand.pop('creation_date')

# print(brand['international_competitors'][-1])

# print(brand['major_color']['US'])

# print(len(brand))

# for key in brand:
#         print(key)

# more_on_zara = {
#         'name': 'Zara',
#         'creation_date': 1975,
#         'creator_name': 'Amancio Ortega Gaona',
#         'type_of_clothes': ['men', 'women', 'children', 'home'],
#         'international_competitors': ['Gap', 'H&M', 'Benetton'],
#         'number_stores': 10000,
#         'major_color': { 
#                         'France': 'blue', 
#                         'Spain': 'red', 
#                         'US': ['pink', 'green']
#                         }
#         }

# brand.update(more_on_zara)
# print(brand['number_stores'])


# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# dict_i = dict(zip(keys, values))
# print(dict_i)

# users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
# dict_d = {}
# for i, char in enumerate(users):
#      dict_d[char] = i
# print(dict_d)

# new_dict = {}
# for i, char in dict_d.items():
#     new_dict[char] = i
# print(new_dict)

# another_dict = {}
# new_users = sorted(users)
# for i, char in enumerate(new_users):
#      another_dict[char] = i
# print(another_dict)

# word = input('Type some word: ')
# dict_word = {}
# for i, char in enumerate(word):
#     dict_word[i] = char
# print(dict_word)


        

# print(new_dict)


# users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
# dict_d = {}
# for i, char in enumerate(users):
#      dict_d[char] = i
# print(dict_d)

# new_dict = {}
# for i, char in dict_d.items():
#     new_dict[char] = i
# print(new_dict)

# another_dict = {}
# new_users = sorted(users)
# for i, char in enumerate(new_users):
#      another_dict[char] = i
# print(another_dict)

# newone_dict = []
# for name in users:
#      if 'i' in name:
#         newone_dict.append(name)
# print(newone_dict)

# newone_dict_1 = []
# for name in users:
#      if 'M' in name[0]:
#         newone_dict_1.append(name)
#      elif 'P' in name[0]:
#         newone_dict_1.append(name)
# print(newone_dict_1)


# new_dict_word = {}
# for i, char in new_dict_word.items():
#     new_dict_word[char] = i
# print(new_dict_word)



# word = input('Type some word: ')
# dict_word = {}
# for i, char in enumerate(word):
#     dict_word[i] = char
# print(dict_word)

# new_dict_word = {}
# for key, value in dict_word.keys():
#     if value not in new_dict_word:
#         new_dict_word[value] = word.count(value)

        

###DC_1
# word = input('Type some word: ')
# new_dict_word = {}
# for f in word:
#     if not f in new_dict_word.keys():
#         new_dict_word[f] = word.count(f)

        
# print(new_dict_word)


items_purchase = {
                "Water": "$1",
                "Bread": "$3",
                "TV": "$1,000",
                "Fertilizer": "$20"
                }

wallet = "$300"

new_pack = items_purchase.values()
newone_dict = []
for name in new_pack:
     if '$' in name:
          
        
print(newone_dict)
