from django.contrib import admin

from viewer.models import Genre, Movie, Country

admin.site.register(Country)
admin.site.register(Genre)
admin.site.register(Movie)
