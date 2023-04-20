from django.shortcuts import render

from django.http import HttpResponse
from datetime import date, datetime
# Create your views here.
# Backend + Frontend = views

# def index(request):
#     return HttpResponse("<h1> This is homepage </h1>")

def index(request):
    current_time = date.today()
    current_hour = datetime.now().hour
    context = {'weather': 'warm', 
               'current_date': current_time, 
               'current_hour': current_hour }
    
    return render(request, 'index.html', context)

def profile(request):
    context = {'name': 'Yossi', 'gender': 'F', 'hobbies': ['Running', 'Codding']}

    return render(request, 'profile.html', context)




