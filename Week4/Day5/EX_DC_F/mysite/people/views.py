from django.shortcuts import render
import json
# Create your views here.


filename = '/Users/sergeiboiko/Study/DI-Bootcamp-Stage1/Week4/Day5/EX_DC_F/mysite/people/people_data.json'

with open(filename, 'r') as f:
    data = json.load(f)

# data_1 = sorted(data, key=lambda i: i['age'])
# print(data_1)
# context={}
# context['people'] = data_1
# print(context)


def people(request):
    data_1 = list(sorted(data, key=lambda i: i['age']))
    context = {}
    context['people'] = data_1
    return render(request, 'people.html', context)


def people_id(request, person: int):
    data_1 = list(sorted(data, key=lambda i: i['age']))
    data_2 = [i for i in data_1 if i['id'] == person]
    context={}
    context['people'] = data_2
    return render(request, 'people_id.html', context)