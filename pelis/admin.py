from django.contrib import admin
from .models import Genre, Movie, Comment

# Register your models here.
admin.site.register(Genre)
#admin.site.register(Movie)
admin.site.register(Comment)

class CommentInline(admin.TabularInline):
    model = Comment

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_genre', 'post_user', 'post_date')
    list_filter = ('genre', 'post_user', 'post_date')
    inlines = [CommentInline]
