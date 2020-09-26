from django.contrib import admin
from .models import Genre, Movie


class GenereAdmin(admin.ModelAdmin):
    list_display('id', 'name')


admin.site.register(Genre, GenereAdmin)
admin.site.register(Movie)
