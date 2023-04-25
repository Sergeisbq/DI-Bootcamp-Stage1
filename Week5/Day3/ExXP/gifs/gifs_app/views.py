from django.shortcuts import render
from .forms import AddGifForm, AddCategory
from .models import *


menu = [{'title': "Home", 'url_name': 'home'},
        {'title': "Add gif", 'url_name': 'add_gif'},
        {'title': "Add category", 'url_name': 'add_category'},
]


# Create your views here.

def home(request):
    gif_list = Gif.objects.all()
    context = {'menu':menu, 'gif_list':gif_list}
    for p in gif_list:
        print(p.url)
    print ('Вызываем форму', context)
    return render(request, 'gifs/home.html', context)


def add_gif(request):
    if request.method == 'POST':
        f = AddGifForm(request.POST)
        if f.is_valid():
            gif_base_object = Gif(title = f.cleaned_data['title'], url = f.cleaned_data['url'], uploader_name = f.cleaned_data['uploader_name'], created_at = f.cleaned_data['created_at'])
            gif_base_object.save()
            gif_base_object.category_set.add(f.cleaned_data['categories'])
            f = AddGifForm()
    else:
        f = AddGifForm()
    context = {'form':f, 'menu':menu}
    return render(request, 'gifs/adding_gif.html', context)


def add_category(request):
    if request.method == 'POST':
        f = AddCategory(request.POST)
        if f.is_valid():
            category_base_object = Category(name = f.cleaned_data['category'])
            category_base_object.save()
            f=AddCategory()
    else:
        f = AddCategory()
    category_list = Category.objects.all()
    context={'form':f, 'menu':menu, 'category_list':category_list}
    return render(request, 'gifs/add_category.html', context)


def category(request, c_id):
    cat_name = Category.objects.get(pk = c_id)
    gif_list = Gif.objects.filter(category__pk = c_id)
    context = {'menu':menu, 'cat_name':cat_name, 'gif_list':gif_list}
    for p in gif_list:
        print(p.url)
    print ('Вызываем форму', context)
    return render(request, 'gifs/category.html', context)