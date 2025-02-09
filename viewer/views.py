from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, ListView

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


class GenresView(View):
    def get(self, request):
        return render(request,
                      "genres.html",
                      {'genres': Genre.objects.all()})


class GenresTemplateView(TemplateView):
    template_name = "genres.html"
    extra_context = {'genres': Genre.objects.all()}


class GenresListView(ListView):
    template_name = "genres.html"
    model = Genre
    # pozor, do template se posílají data pod názvem 'object_list'
    # nebo můžu přejmenovat
    context_object_name = 'genres'


def genre(request, pk):
    if Genre.objects.filter(id=pk).exists():
        return render(request,
                      "genre.html",
                      {'genre': Genre.objects.get(id=pk)})
    return redirect('genres')
