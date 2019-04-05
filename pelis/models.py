from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models  import User
from datetime import date
import uuid

# Create your models here.
class Genre(models.Model):
    """
    Modelo que representa un género literario (p. ej. ciencia ficción, poesía, etc.).
    """
    name = models.CharField(max_length=200, help_text="Enter a movie genre")

    def __str__(self):
        """
        Cadena que representa a la instancia particular del modelo (p. ej en el sitio de Administración)
        """
        return self.name

class Movie(models.Model):
    """
    Modelo que representa una película.
    """
    RATING_CHOICES = ((1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10),)
    title = models.CharField(max_length=200, help_text="Enter the movie title")
    year_of_edit = models.IntegerField(null=True, blank=True, help_text="Enter the year when the movie was edited")
    description = models.TextField(max_length=2000, null=True, blank=True, help_text="Enter a description, synopsis or whatever of the movie")
    director = models.CharField(max_length=200, null=True, blank=True, help_text="Enter the movie director")
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this movie")
    rating = models.IntegerField(null=True, blank=True, choices=RATING_CHOICES, help_text="Rate the movie")
    post_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    in_netflix = models.BooleanField(help_text="Is the movie in Netflix?")
    movie_country = models.CharField(max_length=200, null=True, blank=True, help_text="Enter the movie country")
    post_date = models.DateField(null=True, blank=True)
    image_url = models.CharField(max_length=250, null=True, blank=True, help_text="Enter a movie image link")
    seen_users = models.ManyToManyField(User, related_name='have_seen')

    class Meta:
        ordering = ["post_date", "title"]

    def __str__(self):
        return f'{self.title} ({self.year_of_edit})'

    def display_movie(self):
        return f'{self.title} ({self.year_of_edit})'

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de Movie
        """
        return reverse('movie-detail', args=[str(self.id)])

    def display_genre(self):
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
    display_genre.short_description = 'Genre'

    def has_img(self):
        if self.image_url == "None":
            hasimg = False
        else:
            hasimg = True
        return hasimg

class Comment(models.Model):
    """Modelo que representa un comentario en una película"""
    movie = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True)
    comment_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField(max_length=2000, null=True, blank=True, help_text="Enter your comment about the movie")
    comment_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.comment_user.username} ({self.comment_date})'
