from django import forms 
from .models import Customer, Dishes, Restaurant, Menu, Allergens



class CustomerForm(forms.ModelForm):

    class Meta: 
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'user')
        widgets = {
            'user': forms.HiddenInput()
        }
        
    allergens = forms.ModelMultipleChoiceField(queryset=Allergens.objects.all()) 


class RestAddForm(forms.ModelForm):

    class Meta: 
        model = Restaurant
        fields = ('name', 'address')



class SomeForm(forms.Form):

    customer = forms.ModelChoiceField(queryset=Customer.objects.all().order_by('-id'))



class DishForm(forms.Form):

    dishes = forms.ModelChoiceField(queryset=Dishes.objects.all())

class RestForm(forms.Form):

    rests = forms.ModelChoiceField(queryset=Restaurant.objects.all())








    