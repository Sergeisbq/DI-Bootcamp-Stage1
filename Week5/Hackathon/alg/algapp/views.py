from django.shortcuts import render
from .forms import CustomerForm, SomeForm, DishForm
from .models import Customer, Dishes, Restaurant, Menu
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse, reverse_lazy

# Create your views here.

menu =   [{'title': "Home",          'url_name': 'home_path'},

]

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
    


# def get_cust_and_rest(request):

#     if request.method == 'POST':

#         cust_and_rest = SomeForm(request.POST) # put the data from the request into the ModelForm

#         if cust_and_rest.is_valid(): # check if all fields contain the correct data
            
            
#             customer = cust_and_rest.cleaned_data['customers'] # <QuerySet [<Category: animals>]>
#             restaurant = cust_and_rest.cleaned_data['restaurants'] # <QuerySet [<Category: animals>]>


#             print("customer:", customer)
#             print("restaurant:", restaurant)
#             context = {"customer:", customer,
#                        "restaurant:", restaurant}
#             return HttpResponse("SUCCESSFULLY SAVED")
        
#         else:
#             print(cust_and_rest.errors)
#             return HttpResponse(cust_and_rest.errors)

#     # GET mode - getting content out
#     if request.method == 'GET':
#         cust_and_rest = SomeForm()
#         if cust_and_rest.is_valid(): # check if all fields contain the correct data
            
#             customer = cust_and_rest.cleaned_data['customers'] # <QuerySet [<Category: animals>]>
#             restaurant = cust_and_rest.cleaned_data['restaurants'] # <QuerySet [<Category: animals>]>
#             return (customer, restaurant)
#         print("GET data: ", request.GET) # data associated with the GET method
#         print("GETTING DATA OUT")
#         context = {'form': cust_and_rest}
#         return render(request, 'algapp/choose_c_r.html', context)

# customer, restaurant = get_cust_and_rest()

# if customer is not None and restaurant is not None:
#     print(customer, restaurant)
# else:
#     pass

# class PostCreateView(generic.CreateView):

#     template_name = 'algapp/choose_c_r.html'
#     model = Customer
#     form_class = SomeForm
#     success_url = reverse_lazy("algapp/choose_dish.html")




def get_cust_and_rest(request):

    if request.method == 'POST':
        form_filled = SomeForm(request.POST)
        if form_filled.is_valid():
            customer = form_filled.cleaned_data['customer']
            restaurant = form_filled.cleaned_data['restaurant']
            
            menus = restaurant.menus.all()
            dishes = [menu.dish_id.all()[0] for menu in menus]
            print(dishes)
            dishes_allergic = [is_allergic(customer.id, dish.id) for dish in dishes]

            dishes_allergend = list(zip(dishes, dishes_allergic))

            context = {'dishes_allergens': dishes_allergend, }

            return render(request, 'algapp/choose_dish.html', context)

    if request.method == 'GET':

        cust_and_rest = SomeForm()

        context = {'form': cust_and_rest}

        return render(request, 'algapp/choose_c_r.html', context)



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
