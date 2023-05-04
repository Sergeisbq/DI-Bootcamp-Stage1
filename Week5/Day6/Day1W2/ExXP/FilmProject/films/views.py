from django.shortcuts import render
from .forms import AddFilmForm, AddDirectorForm
from .models import Director, Film, Category, Country
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse, reverse_lazy


# Create your views here.

def home(request):
    films = Film.objects.all()
    directors = Director.objects.all()
    context = {
        'title':'Home page',
        'films': films,
    }
    return render(request, 'homepage.html', context)


class addFilm(generic.CreateView):

    template_name = 'film/addfilm.html'
    model = Film
    form_class = AddFilmForm
    success_url = reverse_lazy("addfilm")



def add_director(request):
        
    if request.method == 'POST':
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$")
        film_filled_form = AddDirectorForm(request.POST) # put the data from the request into the ModelForm

        if film_filled_form.is_valid(): # check if all fields contain the correct data
            # save data into database

            first_name = film_filled_form.cleaned_data['first_name']
            last_name = film_filled_form.cleaned_data['last_name']
            films = film_filled_form.cleaned_data['films']

            new_dir = Director(first_name = first_name, last_name = last_name)
            new_dir.save()
            new_dir.films.add(*films)
            film_filled_form.save()
            print(new_dir)
            # new_film.save()
            
        else:
            pass

        return HttpResponseRedirect('director/adddirector.html')

        # GET mode - getting content out
    if request.method == 'GET':
        film_filled_form = AddDirectorForm()
        print("GET data: ", request.GET) # data associated with the GET method
        print("GETTING DATA OUT")
        context = {'form': film_filled_form}
        return render(request, 'director/adddirector.html', context)
