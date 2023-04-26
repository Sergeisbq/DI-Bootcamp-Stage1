from django.shortcuts import render
from .models import Person
from .forms import SearchForm
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


def search_by_np(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            name_1 = Person(name = form.cleaned_data['name'])
            phone_1 = Person(phone_number = form.cleaned_data['phone_number'])
            # phone_1 = Person(phone_number = form.cleaned_data['phone_number'])
            print(phone_1.phone_number)
            print(name_1.name)
            if Person.objects.filter(name = name_1.name):
                print(name_1.name)
                return name_view(request, name_1.name)
                # name_view(request, name_1.name)
            elif Person.objects.filter(phone_number = phone_1.phone_number):
                print(phone_1.phone_number)
                return phone_view(request, phone_1.phone_number)
            
            # print(phone_1.phone_number)
        # if search_form.is_valid():
        #     objects_n = Person(name = search_form.cleaned_data['name'])
        #     # objects_p = SearchForm(phone_number = search_form.cleaned_data['phone_number'])
        #     print(objects_n)
        #     # print(objects_p)
        #     # category_base_object.save()
        #     # f=AddCategory()

        context = {'form': form}
        
        # getting_data_n = search_form.name
        # getting_data_p = search_form.phone

    #     context = {'person': name_1.name}
    # return render(request, 'name.html', context)
        


    return render(request, 'person.html', context)


# def add_category(request):
#     if request.method == 'POST':
#         f = AddCategory(request.POST)
#         if f.is_valid():
#             category_base_object = Category(name = f.cleaned_data['category'])
#             category_base_object.save()
#             f=AddCategory()
#     else:
#         f = AddCategory()
#     category_list = Category.objects.all()
#     context={'form':f, 'menu':menu, 'category_list':category_list}
#     return render(request, 'gifs/add_category.html', context)