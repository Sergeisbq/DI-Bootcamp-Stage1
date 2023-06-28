from django import forms 
from .models import Customer, Dishes, Restaurant, Menu, Allergens, Ingredients, DishesIng



class CustomerForm(forms.ModelForm):

    class Meta: 
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'user')
        widgets = {
            'user': forms.HiddenInput(),
            # 'allergens': forms.ModelMultipleChoiceField(queryset=Allergens.objects.all())
        }
        
    allergens = forms.ModelMultipleChoiceField(queryset=Ingredients.objects.all().order_by('name')) 


class RestAddForm(forms.ModelForm):

    class Meta: 
        model = Restaurant
        fields = ('name', 'address')
        widgets = {
            'user': forms.HiddenInput(),
        }



class SomeForm(forms.Form):

    customer = forms.ModelChoiceField(queryset=Customer.objects.all().order_by('-id'))



class DishForm(forms.Form):

    dishes = forms.ModelChoiceField(queryset=Dishes.objects.all())

class DishAddForm(forms.ModelForm):

    class Meta: 
        model = DishesIng
        fields = ('name',)
        # widgets = {
        #     'user': forms.HiddenInput(),
        # }
    dish_main_ingredients = forms.ModelMultipleChoiceField(queryset=Ingredients.objects.all().order_by('name')) 
    dish_var_ingredients = forms.ModelMultipleChoiceField(queryset=Ingredients.objects.all().order_by('name'))

class RestForm(forms.Form):

    rests = forms.ModelChoiceField(queryset=Restaurant.objects.all())


class IngAddForm(forms.ModelForm):

    class Meta: 
        model = Ingredients
        fields = ('name',)









    