from django.shortcuts import render
from .forms import TodoForm
from .models import Category, Todo
from django.http import HttpResponse

# Create your views here.


def add_todo_view(request):
    
    # GET mode - getting data/content out
    

    if request.method == 'POST':
        print('POST DATA: ', request.POST) # data associated with the POST method
        print('POSTING DATA')
        todo_filled_form = TodoForm(request.POST) # put the data from the request into the ModelForm

        if todo_filled_form.is_valid(): # check if all fields contain the correct data
            todo_filled_form.save() # new_todo = # save data into database

            # category = todo_filled_form.cleaned_data['category']
            # print('Category', category)
            # category_obj = Category.objects.get(name = category)

            # new_todo.category.add(category_obj)

            return HttpResponse('Successfully saved')


        else:
            return HttpResponse(todo_filled_form.errors)

    if request.method == 'GET':
        todo_form = TodoForm()
        print('GET DATA: ', request.GET) # data associated with the GET method
        print('GETTING DATA OUT')
        context = {'form': todo_form}


    return render(request, 'add_todo.html', context)



def all_todo_view(request):
    todo_list = Todo.objects.all().order_by('pk')
    context = {'todo_list': todo_list}

    return render(request, 'all_todo.html', context)
