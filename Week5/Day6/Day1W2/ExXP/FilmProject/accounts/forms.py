from django import forms

from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm

class ProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = '__all__'
        widgets = {
            'user': forms.HiddenInput()
        }


class CustomSingUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']