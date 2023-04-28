from django.shortcuts import render
from .models import *

# Create your views here.

menu = [{'title': "Home", 'url_name': 'home'},
]

def home(request):
    context = {'menu': menu}
    return render(request, 'home.html', context)


