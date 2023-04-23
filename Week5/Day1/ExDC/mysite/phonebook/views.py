from django.shortcuts import render
from .models import Person
# Create your views here.


def name_view(request, name):
    person = Person.objects.get(name = name)
    context = {'person': person}
    return render(request, 'name.html', context)


def phone_view(request, phone_number):
    person = Person.objects.get(phone_number = phone_number)
    context = {'person': person}
    return render(request, 'phone.html', context)