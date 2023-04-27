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

urlpatterns = [
    # path('add_page/', ,'add_page_name' views.persons),
    path('home', views.home, name = 'home'),
    path('add_page', views.add_gif, name = 'add_gif'),
    path('add_category', views.add_category, name = 'add_category'),
    path('category/<int:c_id>/', views.category, name = 'category_path'),
    path('gifs_all', views.gifs_view, name = 'gifs_view'),
]