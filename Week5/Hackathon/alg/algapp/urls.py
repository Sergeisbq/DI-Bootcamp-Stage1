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
from .views import add_customer_view, all_rest, rest, one_rest, add_rest_view, from_one_rest_to #choose_dish, get_cust_and_rest


urlpatterns = [
    path('', views.home, name="home_path"),
    path("add_customer/", add_customer_view),
    # path("choose_c_r/", get_cust_and_rest), 
    path("restaurants/", rest, name='restaurants'), 
    path("add_restaurant/", add_rest_view, name='add_restaurant'), 
    path("restaurant/<int:r_id>", from_one_rest_to, name='restaurant'), #one_rest
    path("choose_dish/", from_one_rest_to, name='dish_path'), 
    # path("restaurant/<int:r_id>", rest, name='restaurant'),
    # path('rentals_list/', views.rentals_list, name="rentals_list_path" ),
    # path('rental/<int:r_id>', views.rental, name="rental_path" ),
    # path('customer/<int:c_id>', views.customer, name="customer_path"),
    # path('vehicle/<int:v_id>', views.vehicle, name="vehicle_path"),
]