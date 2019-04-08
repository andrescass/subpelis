from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Movie, Comment
from tinymce.widgets import TinyMCE


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class NewMovieForm(forms.ModelForm):
    description = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = Movie
        fields = ('title', 'year_of_edit', 'director', 'genre', 'movie_country', 'description', 'image_url', 'in_netflix', 'rating',)

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        labels = {
            'content': ('New Comment:'),
        }

class UpdateMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('title', 'year_of_edit', 'director', 'genre', 'movie_country', 'description', 'image_url', 'in_netflix', 'rating',)
