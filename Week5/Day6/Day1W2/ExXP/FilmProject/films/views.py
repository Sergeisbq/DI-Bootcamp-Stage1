from django.shortcuts import render, redirect
from .forms import AddFilmForm, AddDirectorForm, CommentForm
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

    model = Film
    # form_class = AddFilmForm
    template_name = 'film/addfilm.html'
    success_url = reverse_lazy("addfilm")

    def get_context_data(self, **kwargs):

        films = Film.objects.all()
        form_class = AddFilmForm
        context = {'films': films,
                   'form': form_class}
        return context




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
        dir_filled_form = AddDirectorForm()
        print("GET data: ", request.GET) # data associated with the GET method
        print("GETTING DATA OUT")
        directors = Director.objects.all()
        context = {'form': dir_filled_form,
                   'directors': directors}
        return render(request, 'director/adddirector.html', context)
    

# class DirectorDeleteView(DeleteView):

#     template_name = 'director/deldirector.html'
#     model = Director
#     success_url = reverse_lazy('homepage')
#     messages.add_message(request, messages.INFO, "Hello world.")


class DirectorDeleteView(DeleteView):

    model = Director
    template_name = 'director/deldirector.html'
    success_url = reverse_lazy('homepage')

    def delete(self, request, *args, **kwargs):

        messages.success(request, 'Director deleted successfully!')
        return super().delete(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = messages.get_messages(self.request)
        return context


class FilmDeleteView(DeleteView):

    model = Film
    template_name = 'film/delfilm.html'
    success_url = reverse_lazy('homepage')

    def delete(self, request, *args, **kwargs):

        messages.success(request, 'Film deleted successfully!')
        return super().delete(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = messages.get_messages(self.request)
        return context
    


def add_comment(request):

    # film = Film.objects.get(pk=pk)
    # print(film)
    # field_form = CommentForm()
    if request.method == 'POST':
        print("ADD COMMENT:", request.POST)
        field_form = CommentForm(request.POST)
        print('SMTH')
        if field_form.is_valid():
            print('SMTH')
            comment = field_form.save(commit=False)
            # comment.film = film
            comment.save()
            
            print("SUCCESSFULLY ADDED COMMENT")
            return redirect('homepage')
    else:
        field_form = CommentForm()

        return render(request, 'film/addcomment.html', {'form': field_form})
        


    # if request.method == 'POST':
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         comment = form.save(commit=False)
    #         comment.film = film
    #         comment.save()
    #         return redirect('film_detail', pk=film.pk)
    # else:
    #     form = CommentForm()

    # return render(request, 'add_comment.html', {'form': form})
