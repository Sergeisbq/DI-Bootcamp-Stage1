from django import forms 
from .models import Customer, Dishes, Restaurant, Menu, Allergens



class CustomerForm(forms.ModelForm):

    class Meta: 
        model = Customer
        fields = ('first_name', 'last_name', 'email')
        
    allergens = forms.ModelMultipleChoiceField(queryset=Allergens.objects.all()) 


class SomeForm(forms.Form):

    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    restaurant = forms.ModelChoiceField(queryset=Restaurant.objects.all()) 


class DishForm(forms.Form):

    dishes = forms.ModelChoiceField(queryset=Dishes.objects.all())








    