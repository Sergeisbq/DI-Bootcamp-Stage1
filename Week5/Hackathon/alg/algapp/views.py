from django.shortcuts import render
from .forms import CustomerForm, SomeForm, DishForm, RestForm, RestAddForm
from .models import Customer, Dishes, Restaurant, Menu
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse, reverse_lazy
import random

# Create your views here.



def home (request):
    context={'title':'Home page'}
    return render(request, 'algapp/home.html', context)



def add_customer_view(request):

    if request.method == 'POST':

        customer_filled_form = CustomerForm(request.POST) # put the data from the request into the ModelForm

        if customer_filled_form.is_valid(): # check if all fields contain the correct data
            new_customer = customer_filled_form.save() # save data into database
            
            allergens = customer_filled_form.cleaned_data['allergens'] # <QuerySet [<Category: animals>]>

            new_customer.allergens.add(*allergens)  # [<Category: animals>, <Category: funny>]

            print("allergens:", allergens)
            return HttpResponse("SUCCESSFULLY SAVED")
        
        else:
            print(customer_filled_form.errors)
            return HttpResponse(customer_filled_form.errors)

    # GET mode - getting content out
    if request.method == 'GET':
        customer_filled_form = CustomerForm()
        print("GET data: ", request.GET) # data associated with the GET method
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
                # Menu.restaurant_id.add(*restaurant_id_to_add)
                # Menu.objects.create(restaurant_id = restaurant_id_to_add, dish_id = dish_id_to_add)
                
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
        print("GET data: ", request.GET) # data associated with the GET method
        print("GETTING DATA OUT")
        context = {'form': rest_filled_form}
        return render(request, 'algapp/add_restaurant.html', context)


# def get_cust_and_rest(request):

#     if request.method == 'POST':
#         form_filled = SomeForm(request.POST)
#         if form_filled.is_valid():
#             customer = form_filled.cleaned_data['customer']
#             restaurant = form_filled.cleaned_data['restaurant']
            
#             menus = restaurant.menus.all()
#             dishes = [menu.dish_id.all()[0] for menu in menus]
#             print(dishes)
#             dishes_allergic = [is_allergic(customer.id, dish.id) for dish in dishes]

#             dishes_allergend = list(zip(dishes, dishes_allergic))

#             context = {'dishes_allergens': dishes_allergend, }

#             return render(request, 'algapp/choose_dish.html', context)

#     if request.method == 'GET':

#         cust_and_rest = SomeForm()

#         context = {'form': cust_and_rest}

#         return render(request, 'algapp/choose_c_r.html', context)



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
            print(f"FOUND ALLERGEN - {allergen}")
            return f"FOUND ALLERGEN - {allergen}"
    return f"This dish is ok for you"

# def choose_dish(request):
#     context = {'customer:': customer1,
#                 'restaurant': restaurant1}

#     return render(request, 'algapp/choose_dish.html', context)

# return_values = get_cust_and_rest(None)
# restaurant1 += return_values[1]
# customer1 += return_values[2]



    

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
 

    
# def one_rest (request, r_id):
    
#     r = Restaurant.objects.get(pk=r_id)
#     menus = r.menus.all()
#     dishes = [menu.dish_id.all()[0] for menu in menus]
    
#     context={'r':r, 'dishes': dishes}
#     return render(request, 'algapp/restaurant.html', context)


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



# def from_one_rest_to(request, r_id):
#     restaurant = Restaurant.objects.get(pk=r_id)
    
#     print(r_id, '@@@@@@@@@')
#     menus = restaurant.menus.all()
#     dishes = [menu.dish_id.all()[0] for menu in menus]
#     if request.method == 'POST':
#         form_filled = SomeForm(request.POST)
#         if form_filled.is_valid():
#             customer = form_filled.cleaned_data['customer']
            
            
#             menus = restaurant.menus.all()
#             dishes = [menu.dish_id.all()[0] for menu in menus]

#             dishes_allergic = [is_allergic(customer.id, dish.id) for dish in dishes]

#             dishes_allergend = list(zip(dishes, dishes_allergic))

#             context = {'dishes_allergens': dishes_allergend, 'r': restaurant}

#             return render(request, 'algapp/choose_dish.html', context)

#     if request.method == 'GET':

#         cust_and_rest = SomeForm()

#         context = {'form': cust_and_rest}

#         return render(request, 'algapp/restaurant.html', context)
    


