from django.contrib import admin

from viewer.models import Genre, Movie, Country, Creator

admin.site.register(Country)
admin.site.register(Creator)
admin.site.register(Genre)
admin.site.register(Movie)
