from django.shortcuts import render
from django.http import HttpRequest
# from .utils import read_data, find_instance
from .models import Animal, Family

# Create your views here.


# def all_animals(request):
#     animals = read_data('/Users/sergeiboiko/Study/DI-Bootcamp-Stage1/Week4/Day5/ExAnimals/mysite/data.json', 'animals')
#     context = {'animals': animals}

#     return render(request, 'animals.html', context)


# def animal(request: HttpRequest, id: int):
#     animals = read_data('/Users/sergeiboiko/Study/DI-Bootcamp-Stage1/Week4/Day5/ExAnimals/mysite/data.json', 'animals')
#     instance = find_instance(animals, id)
#     context = {'animal': instance}
#     return render(request, 'animal.html', context)


def all_animals(request):
    animals_list = Animal.objects.all().order_by('pk')
    context = {'animals': animals_list}

    return render(request, 'animals.html', context)


def animal(request: HttpRequest, id: int):

    animals_instance = Animal.objects.get(id = id)
    context = {'animal': animals_instance}
    return render(request, 'animal.html', context)


def all_families(request):
    family_list = Family.objects.all().order_by('pk')
    context = {'family': family_list}

    return render(request, 'families.html', context)


def family(request: HttpRequest, id: int):

    family_instance = Family.objects.get(id = id)
    context = {'family': family_instance}
    return render(request, 'family.html', context)