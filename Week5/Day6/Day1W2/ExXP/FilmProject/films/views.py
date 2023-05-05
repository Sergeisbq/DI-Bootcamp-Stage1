from django.shortcuts import render, redirect
from .forms import AddFilmForm, AddDirectorForm
from .models import Director, Film, Category, Country
from django.views.generic.edit import DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib import messages 
from django.urls import reverse, reverse_lazy


# Create your views here.

def home(request):
    films = Film.objects.all()
    directors = Director.objects.all()
    context = {
        'title':'Home page',
        'films': films,
        'directors': directors
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
            # film_filled_form.save()
            print(new_dir)

            
        else:
            pass

        return redirect('adddirector')

        # GET mode - getting content out
    if request.method == 'GET':
        film_filled_form = AddDirectorForm()
        print("GET data: ", request.GET) # data associated with the GET method
        print("GETTING DATA OUT")
        directors = Director.objects.all()
        context = {'form': film_filled_form,
                   'directors': directors}
        return render(request, 'director/adddirector.html', context)
    

# class DirectorDeleteView(DeleteView):

#     template_name = 'director/deldirector.html'
#     model = Director
#     success_url = reverse_lazy('homepage')
#     messages.add_message(request, messages.INFO, "Hello world.")


class DirectorDeleteView(DeleteView):

    model = Director
    success_url = reverse_lazy('homepage')
    template_name = 'director/deldirector.html'

    def delete(self, request, *args, **kwargs):

        messages.success(request, 'Director deleted successfully!')
        return super().delete(request, *args, **kwargs)


# class FilmDeleteView(DeleteView):
#     template_name = 'film/delfilm.html'
#     model = Film
#     success_url = reverse_lazy('sfd')

