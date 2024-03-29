from django import forms
from .models import Post, Comment
from django.core.exceptions import ValidationError 

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'author': forms.HiddenInput(attrs={'readonly': 'readonly'}),
            'date_created': forms.DateInput(attrs={'type': 'date'}) #'class': 'form-control', 
            }
        
    def clean_title(self):

        title = self.cleaned_data['title']
        if title.startswith('A'):
            raise ValidationError("The title should not start with letter 'A'")
        return title
    
    def clean(self):
        cleaned_data = super().clean()
        author = cleaned_data['author']
        title = cleaned_data['title']

        if author.user.username.lower() == 'ben':
            if title.lower() == 'test':
                raise ValidationError("User cannot be Ben and write the 'Test' post")
            


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'
        widgets = {
            'post': forms.HiddenInput(),
            'author': forms.HiddenInput(),
            'content': forms.Textarea()
        }
