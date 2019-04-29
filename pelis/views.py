from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic.edit import FormMixin
from .models import Movie, Genre, Comment
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_protect
from .forms import SignUpForm, NewMovieForm, NewCommentForm, UpdateMovieForm
from django.utils import timezone
from django.urls import reverse

# Create your views here.
class MovieListView(generic.ListView):
    model = Movie
    paginate_by = 20

class MovieDetailView(FormMixin, generic.DetailView):
    model = Movie
    form_class = NewCommentForm

    def get_success_url(self):
        return reverse('movie-detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(MovieDetailView, self).get_context_data(**kwargs)
        context['form'] = NewCommentForm(initial={'post': self.object})
        return context

    def post(self, request, pk, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        movie = get_object_or_404(Movie, pk=pk)
        if form.is_valid():
            return self.form_valid(form, request, movie)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, request, movie):
        comment = form.save(commit=False)
        comment.content = form.cleaned_data.get('content')
        comment.comment_user = request.user
        comment.comment_date = timezone.now()
        comment.movie = movie
        comment.save()
        return super(MovieDetailView, self).form_valid(form)

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

def update_movie(request, pk):
    movie_inst = get_object_or_404(Movie, pk = pk)
    if request.method == "POST":
        form = UpdateMovieForm(request.POST, instance=movie_inst)
        if form.is_valid():
            form.save()
            return redirect('movie-detail', pk=movie_inst.pk)
    else:
        form = UpdateMovieForm(instance=movie_inst)
    return render(request, 'pelis/update_movie.html', {'form': form, 'movie_inst': movie_inst})
