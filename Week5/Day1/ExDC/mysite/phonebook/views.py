from django.shortcuts import render
from .models import Person
# Create your views here.


def search(model, value):

    result = None
    try:
        model_instance = model.objects.get(name = value)
        result = model_instance
    except model.DoesNotExist:
        pass
    try:
        model_instance = model.objects.get(phone_number = value)
        result = model_instance
    except model.DoesNotExist:
        pass

    return result


def search_person(request, search_value: str):

    context = {}

    person_info = search(Person, search_value)

    if person_info is not None:
        context = {'person': person_info}

    return render(request, 'person_info.html', context)


def name_view(request, name):
    person = Person.objects.get(name = name)
    context = {'person': person}
    return render(request, 'name.html', context)


def phone_view(request, phone_number):
    person = Person.objects.get(phone_number = phone_number)
    context = {'person': person}
    return render(request, 'phone.html', context)


def profile_view(request, search_value: str):
    context = {}
    person_info = search(Person, search_value)

    if person_info is not None:
        person_profile = person_info.profile
        person_languages = person_profile.languages.all()

        context = {'person_info': person_info, 'person_profile': person_profile, 'languages': person_languages}

    return render(request, 'profile.html', context)