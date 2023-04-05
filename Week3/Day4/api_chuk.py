import requests
import time
import json

database = []
while len(database) < 10:
    response_jokes = requests.get('https://api.chucknorris.io/jokes/random?category=science')
    print(response_jokes)
    data_3 = response_jokes.json()
    database.append(data_3)
    time.sleep(0.5)

filename = "data_chuk.json"
with open(filename, 'w') as file:
    json.dump(database, file)

for i in range(len(database)):
    print(f"{i+1}. {database[i]['value']}")
