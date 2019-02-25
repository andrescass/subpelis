from django.shortcuts import render, redirect
from django.views import generic
from .models import Movie, Genre, Comment
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect
from .forms import SignUpForm, NewMovieForm
from django.utils import timezone

# Create your views here.
class MovieListView(generic.ListView):
    model = Movie
    paginate_by = 10

class MovieDetailView(generic.DetailView):
    model = Movie

@csrf_protect
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def new_movie(request):
    if request.method == "POST":
        form = NewMovieForm(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.post_user = request.user
            movie.post_date = timezone.now()
            movie.save()
            return redirect('movie-detail', pk=movie.pk)
    else:
        form = NewMovieForm()
    return render(request, 'pelis/new_movie.html', {'form': form})
