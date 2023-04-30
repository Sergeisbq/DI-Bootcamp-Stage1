from django import forms 
from .models import Customer, Dishes, Restaurant, Menu, Allergens


class CustomerForm(forms.ModelForm):

    class Meta: 
        model = Customer
        fields = ('first_name', 'last_name', 'email')
        
    allergens = forms.ModelMultipleChoiceField(queryset=Allergens.objects.all()) 
    