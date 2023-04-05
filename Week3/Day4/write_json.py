import json

data = {
    'weather': 'cool',
    'temperature': 243,
    'numbers': [1,2,3,4]
}

filename = 'data.json'

with open(filename, 'w') as file:
    json.dump(data, file)