# Generated by Django 2.1.5 on 2019-02-19 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, help_text='Enter your comment about the movie', max_length=2000, null=True)),
                ('comment_date', models.DateField(blank=True, null=True)),
                ('comment_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a movie genre', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter the movie title)', max_length=200)),
                ('year_of_edit', models.IntegerField(blank=True, help_text='Enter the year when the movie was edited', null=True)),
                ('description', models.TextField(blank=True, help_text='Enter a description, synopsis or whatever of the movie', max_length=2000, null=True)),
                ('director', models.CharField(blank=True, help_text='Enter the movie director)', max_length=200, null=True)),
                ('rating', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], help_text='Enter the year when the movie was edited', null=True)),
                ('in_netflix', models.BooleanField(help_text='Is the movie in Netflix?')),
                ('movie_country', models.CharField(blank=True, help_text='Enter the movie country)', max_length=200, null=True)),
                ('post_date', models.DateField(blank=True, null=True)),
                ('image_url', models.CharField(blank=True, help_text='Enter a movie image link)', max_length=250, null=True)),
                ('genre', models.ManyToManyField(help_text='Select a genre for this movie', to='pelis.Genre')),
                ('post_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pelis.Movie'),
        ),
    ]