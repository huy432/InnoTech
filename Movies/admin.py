from django.contrib import admin
from .models import Film, Chapter

# Register your models here.
class FilmView(admin.ModelAdmin):
    list_display = ['filmid','title','count']

admin.site.register(Film, FilmView)

class ChapterView(admin.ModelAdmin):
    list_display = ['filmid','chapterid','url']

admin.site.register(Chapter, ChapterView)