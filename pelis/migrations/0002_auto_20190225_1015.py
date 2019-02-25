# Generated by Django 2.1.5 on 2019-02-25 13:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pelis', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['post_date', 'title']},
        ),
        migrations.AddField(
            model_name='movie',
            name='seen_users',
            field=models.ManyToManyField(related_name='have_seen', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(blank=True, help_text='Enter the movie director', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image_url',
            field=models.CharField(blank=True, help_text='Enter a movie image link', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_country',
            field=models.CharField(blank=True, help_text='Enter the movie country', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(help_text='Enter the movie title', max_length=200),
        ),
    ]
