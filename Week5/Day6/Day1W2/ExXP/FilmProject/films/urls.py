"""
URL configuration for gifs_web project.
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from .views import addFilm, add_director, DirectorDeleteView, FilmDeleteView, add_comment



urlpatterns = [
    path('films/homepage/', views.home, name="homepage"),
    path('films/addfilm/', addFilm.as_view(), name="addfilm"),
    path('films/adddirector/', add_director, name="adddirector"),
    path('films/deldirector/<int:pk>', DirectorDeleteView.as_view(), name="deldirector"),
    path('films/delfilm/<int:pk>', FilmDeleteView.as_view(), name="delfilm"),
    path('films/addcomment/', add_comment, name="addcomment")
    
    # path("restaurants/", rest, name='restaurants'), 
    # path("add_restaurant/", add_rest_view, name='add_restaurant'), 
    # path("restaurant/<int:r_id>", one_rest, name='restaurant'), 
    # path("choose_dish/<int:r_id>", one_rest, name='dish_path'), 

]