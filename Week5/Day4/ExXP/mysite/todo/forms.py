from django import forms
from .models import Category, Todo


class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ('title', 'details', 'deadline_date', 'category')


