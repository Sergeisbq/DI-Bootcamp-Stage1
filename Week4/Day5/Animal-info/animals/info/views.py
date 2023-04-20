from django.shortcuts import render
import json
# Create your views here.

filename = '/Users/sergeiboiko/Study/DI-Bootcamp-Stage1/Week4/Day5/Animal-info/animals/info/data_for_ex.json'

with open(filename, 'r') as f:
    data = json.load(f)

animals = data['animals']
families = data['families']

# print(animals[1]['id'])


def animal(request, id):
    animal_selected = ''
    for i in animals:
        if i['id'] == id:
            animal_selected = i
    return render(request, 'animal.html', animal_selected)


def family(request, id):
    family_selected = ''
    for i in families:
        if i['id'] == id:
            family_selected = i
    return render(request, 'family.html', family_selected)
    




