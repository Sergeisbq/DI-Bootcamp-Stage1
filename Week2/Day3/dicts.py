a_set = {1,2,3}

a_dict = {100: "And than smth happpend"}

b_dict = {
    'first_name': 'Yossi',
    'last_name': 'Eik',
    'age': 31,
    
    }

# Get data

print(b_dict['first_name'])

b_dict.get('planet', 'Earth') # Return "Earth" if "planet" not found

# Get the keys
b_dict.keys()

# Get the values
b_dict.values()

# Update

b_dict['country'] = 'Israel' # adds new key and value


b_dict.update ({ 
    'residence': 'Tel Aviv',
    'languages': ['python', 'js', 'html']}) # adds new keys and values

a_dict[100] = "Smth" # change the value of [100] key
print(a_dict)

b_dict.get('planet', 'Earth')
print(b_dict.get('planet', 'Earth'))


# Delete

b_dict.pop('country')
# del b_dict['country']

removed = b_dict.pop('age')
print(removed)


# Loops

b_dict = {
    'first_name': 'Yossi',
    'last_name': 'Eik',
    'age': 31,
    'residence': 'Tel Aviv',
    'languages': ['python', 'js', 'html']
    }

full_name = ""
for key in b_dict:
    print(key)
    if key == 'first_name' or key == 'last_name':
        full_name += f'{b_dict[key]} '

print(full_name)

for value in b_dict.values():
    print(value)

for key, value in b_dict.items():
    print(f"Key: {key}, Value: {value}")



sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

del sample_dict["name"]
del sample_dict["salary"]

print(sample_dict)


# s = 'abcd'
# for char in s:
#     print(char)

# for i, char in enumerate(s):
#     print(i, char)

# alpha = 'abcde'
# eng_dict = {}
# for i, char in enumerate(alpha):
#     eng_dict[i] = char

# eng_dict = dict(enumerate(alpha))


# alpha = 'abcde'
# eng_dict = dict(enumerate(alpha))

# even_letters = [value for key, value in eng_dict.items() if key % 2 == 1]
# print(even_letters)

# even_letters ={key: value for key, value in eng_dict.items() if key % 2 == 1}
# print(even_letters)


# word = "HEllo"

# word_list = [char for char in word if char != 'l']

# print(word_list)


word = "HEllO"

word_dict = {index: value for index, value in enumerate(word)}
print(word_dict)