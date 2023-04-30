from django.shortcuts import render
from .forms import CustomerForm
from .models import Customer, Dishes, Restaurant, Menu
from django.http import HttpResponse

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