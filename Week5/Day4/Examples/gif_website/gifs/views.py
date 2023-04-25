from django.shortcuts import render
from .forms import CategoryForm, GifForm, LikeForm
from .models import Category, Gif
from django.http import HttpResponse

# Create your views here.

def add_gif_view(request):
    
    # GET mode - getting data/content out
    

    if request.method == 'POST':
        print('POST DATA: ', request.POST) # data associated with the POST method
        print('POSTING DATA')
        gif_filled_form = GifForm(request.POST) # put the data from the request into the ModelForm

        if gif_filled_form.is_valid(): # check if all fields contain the correct data
            new_gif = gif_filled_form.save() # save data into database

            category = gif_filled_form.cleaned_data['categories']
            print('Categories', category)
            category_obj = Category.objects.get(name = category)

            new_gif.categories.add(category_obj)

            return HttpResponse('Successfully saved')


        else:
            return HttpResponse(gif_filled_form.errors)

    if request.method == 'GET':
        gif_form = GifForm()
        print('GET DATA: ', request.GET) # data associated with the GET method
        print('GETTING DATA OUT')
        context = {'form': gif_form}


    return render(request, 'add_gif.html', context)


# Add new Category view

def add_category_view(request):

    if request.method == 'POST':
        print('POST DATA: ', request.POST) # data associated with the POST method
        print('POSTING DATA')
        category_filled_form = CategoryForm(request.POST) # put the data from the request into the ModelForm

        if category_filled_form.is_valid(): # check if all fields contain the correct data
            category_filled_form.save() # save daat into database
            return HttpResponse('Successfully saved')


    if request.method == 'GET':
        category_form = CategoryForm()
        print('GET DATA: ', request.GET) # data associated with the GET method
        print('GETTING DATA OUT')
        context = {'form': category_form}

        return render(request, 'add_category.html', context)


def gifs_view(request):

    gifs_all = Gif.objects.all()
    like_dislike_forms = [GifForm(initial={'gif':gif_instance}) for gif_instance in gifs_all]

    gifs_forms = list(zip(gifs_all, like_dislike_forms))

    context = {'gifs_forms': gifs_forms}

    return render(request, 'gifs.html', context)