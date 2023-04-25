from django import forms
from .models import Gif, Category


class GifForm(forms.Form):
    uploader_name = forms.CharField(max_length = 50)
    title = forms.CharField(max_length = 50)
    url = forms.URLField()
    created_at = forms.DateTimeField()


class CategoryForm(forms.Form):
    name = forms.CharField(max_length = 50)

class AddGifForm(forms.Form):
    uploader_name = forms.CharField(max_length=50, label='Name')
    title = forms.CharField(max_length=50)
    url = forms.URLField()
    created_at = forms.DateTimeField()
    categories = forms.ModelChoiceField(queryset = Category.objects.all(), empty_label='choice')


class AddCategory(forms.Form):
    category = forms.CharField(max_length=50)
