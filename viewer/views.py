from django.shortcuts import render, redirect

from viewer.models import Movie, Genre


def home(request):
    return render(request, "home.html")


def movies(request):
    movies_ = Movie.objects.all()
    context = {'movies': movies_}
    return render(request=request,
                  template_name="movies.html",
                  context=context)


def movie(request, pk):
    if Movie.objects.filter(id=pk).exists():
        movie_ = Movie.objects.get(id=pk)
        context = {'movie': movie_}
        return render(request, "movie.html", context)
    return redirect("home")


def genres(request):
    return render(request,
                  "genres.html",
                  {'genres': Genre.objects.all()})
