from django.shortcuts import render

from viewer.models import Movie


def movies(request):
    movies_ = Movie.objects.all()
    for movie_ in movies_:
        print(movie_)
