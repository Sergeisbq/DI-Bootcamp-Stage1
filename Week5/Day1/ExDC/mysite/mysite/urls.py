"""
URL configuration for mysite project.

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
from django.contrib import admin
from django.urls import path
from phonebook.views import name_view, phone_view, search_by_np, profile_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('name_view/<str:name>', name_view, name='name_view'),
    path('phone_view/<str:phone_number>', phone_view, name='phone_view'),
    path('profiles/<str:search_value>', profile_view, name='profile_view'),
    path('person/', search_by_np, name='search_by_np')

]


