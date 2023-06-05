from django.shortcuts import render
from .forms import CustomerForm, SomeForm, DishForm, RestForm, RestAddForm
from .models import Customer, Dishes, Restaurant, Menu, Allergens, Statistic
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse, reverse_lazy
import random
from django.contrib.messages.views import SuccessMessageMixin
import json
import os
import openai
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from dotenv import load_dotenv
load_dotenv()


def home (request):
    context={'title':'Home page'}
    return render(request, 'algapp/home.html', context)



def add_customer_view(request):

    if request.method == 'POST':

        customer_filled_form = CustomerForm(request.POST)

        if customer_filled_form.is_valid(): 
            new_customer = customer_filled_form.save() 
            allergens = customer_filled_form.cleaned_data['allergens']
            new_customer.allergens.add(*allergens) 
            # customer_allergens = Allergens.
            print("allergens:", allergens)
            
            context = {'new_customer': new_customer}
            return render(request, 'profile.html', context)
        
        else:
            print(customer_filled_form.errors)
            return HttpResponse(customer_filled_form.errors)

    if request.method == 'GET':
        customer_filled_form = CustomerForm(initial={"user": request.user})
        print("GET data: ", request.GET)
        print("GETTING DATA OUT")
        context = {'form': customer_filled_form}
        return render(request, 'algapp/add_customer.html', context)
    

def add_rest_view(request):

    if request.method == 'POST':

        rest_filled_form = RestAddForm(request.POST) # put the data from the request into the ModelForm

        if rest_filled_form.is_valid(): # check if all fields contain the correct data
             rest_filled_form.save()# save data into database

             for _ in range(random.randint(12, 18)):

                list_of_dishes = Dishes.objects.all().all().values_list('id', flat=True)
                restaurant_id_to_add_1 = Restaurant.objects.latest('id')
                restaurant_id_to_add = restaurant_id_to_add_1.id
                dish_id_to_add = random.choice(list_of_dishes)
                
                new_menu = Menu()
                new_menu.save()
                new_menu.restaurant_id.add(restaurant_id_to_add)
                new_menu.dish_id.add(dish_id_to_add)

                print(new_menu)
                new_menu.save()
            
                # return HttpResponse("SUCCESSFULLY SAVED")
        
        else:
            pass

        return HttpResponseRedirect('/restaurants')

    # GET mode - getting content out
    if request.method == 'GET':
        rest_filled_form = RestAddForm()
        context = {'form': rest_filled_form}
        return render(request, 'algapp/add_restaurant.html', context)





def is_allergic(customer_id: int, dish_id: int) -> bool:

    person_algens = Customer.objects.get(id=customer_id)
    allergens = person_algens.allergens.all()
    dish = Dishes.objects.get(id=dish_id)
    
    ingredients = dish.dish
    print(customer_id)
    print(allergens)
    print(dish)
    for allergen in allergens:
        if allergen.name in ingredients:
            return f"FOUND ALLERGEN - {allergen}" 
    return None #f"This dish is ok for you"


    

def all_rest(request):

    if request.method == 'POST':
        rest_form = RestForm(request.POST)
        if rest_form.is_valid():
            rest = rest_form.cleaned_data['rests']

            context = {'rest': rest}

            return render(request, 'algapp/restaurant.html', context)

    if request.method == 'GET':

        rest_form = RestForm()

        context = {'form': rest_form}

        return render(request, 'algapp/restaurants.html', context)
    

def rest (request):

    rests = Restaurant.objects.all()
    context={'rests': rests}
    return render(request, 'algapp/restaurants.html', context)
 


def one_rest (request, r_id):
    
    r = Restaurant.objects.get(pk=r_id)
    menus = r.menus.all()
    dishes = [menu.dish_id.all()[0] for menu in menus]
    form_filled = SomeForm()
    if request.method == 'POST':
        form_filled = SomeForm(request.POST)
        if form_filled.is_valid():
            customer = form_filled.cleaned_data['customer']
            menus = r.menus.all()
            dishes = [menu.dish_id.all()[0] for menu in menus]

            dishes_allergic = [is_allergic(customer.id, dish.id) for dish in dishes]

            dishes_allergend = list(zip(dishes, dishes_allergic))
            context = {'dishes_allergens': dishes_allergend, 'r': r}

            return render(request, 'algapp/choose_dish.html', context)
            
    
    context={'r':r, 'dishes': dishes, 'form': form_filled}
    return render(request, 'algapp/restaurant.html', context)



@csrf_exempt
def ask_chatGPT(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    if request.method == 'POST':
        try:
            
            json_data = json.dumps(request.POST)
            data = json.loads(json_data)
            print(data['select_th'])
            api_key = os.getenv('OPENAI_API_KEY')
            openai.api_key = api_key
            promt1 = ''
            if data['select_th'] == 'Recipe':
                promt1 = 'Type a recipe for '
            elif data['select_th'] == 'Suggestion':
                promt1 = 'Reccomend me '
            else:
                promt1 = ''
            allergens = []
            for allergen in customer.allergens.all():
                allergens.append(allergen.name)
            promt2 = f" without {allergens}"
            print(promt2)
            print(promt1 + ' ' + data['prompt'] + promt2 + ' response as a JSON')

            
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=promt1 + ' ' + data['prompt'] + promt2 + ' response as a JSON',
                temperature=0,
                max_tokens=1500,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
                stop=["###"]
            )
            print('This is a prompt ' + promt1 + data['prompt'] + ' response as a JSON')
            json_object = json.dumps(response, indent=4)

            with open("sample.json", "w") as outfile:
                outfile.write(json_object)

            with open('sample.json') as file:
                json_data = json.load(file)
                print(json_data)
                new_data = Statistic()
                new_data.file = json_data
                new_data.save()

                print(json_data['choices'][0]['text'])
                text = json_data['choices'][0]['text']
                print("----here text ----", text)
                context = {'response': json.loads(text)}
                # print(context)

            return render(request, 'algapp/answerOA.html', context)

            # return JsonResponse(response, safe=False)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    else:
        # return JsonResponse({'error': 'Invalid request method'}, status=405)
        return render(request, 'algapp/openai.html', {})


    


