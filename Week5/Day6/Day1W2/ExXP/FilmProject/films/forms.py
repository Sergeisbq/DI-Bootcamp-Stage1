from django import forms
from .models import Director, Film, Category, Country, Comment


class AddFilmForm(forms.ModelForm):

    class Meta: 
        model = Film
        fields = ['title', 'release_date', 'category', 'created_in_country']
        
    # category = forms.ModelChoiceField(queryset=Category.objects.all()) 
    # created_in_country = forms.ModelChoiceField(queryset=Country.objects.all())



class AddDirectorForm(forms.ModelForm):

    class Meta: 
        model = Director
        fields = ('first_name', 'last_name')
        
    films = forms.ModelMultipleChoiceField(queryset=Film.objects.all()) 


class CommentForm(forms.ModelForm):

    class Meta:
        INTEGER_CHOICES= [tuple([x,x]) for x in range(1,6)]
        model = Comment
        fields = ['content', 'rate']
        widgets = {'rate':forms.Select(choices=INTEGER_CHOICES)
                   }
        # widgets = {
        #     'film': forms.HiddenInput(),
        #     'author': forms.HiddenInput(),
        #     'content': forms.Textarea()
        # }