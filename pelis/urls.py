from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.MovieListView.as_view(), name='index'),
    url(r'^movies/$', views.MovieListView.as_view(), name='home'),
    url(r'^movie/(?P<pk>\d+)$', views.MovieDetailView.as_view(), name='movie-detail'),
    url(r'^movies/$', views.MovieListView.as_view(), name='movies'),
    url(r'^newmovie/$', views.new_movie, name='new-movie'),
]
