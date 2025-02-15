from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView

from viewer.forms import CreatorForm
from viewer.models import Movie, Genre, Creator, Country


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


class CreatorsListView(ListView):
    template_name = "creators.html"
    model = Creator
    context_object_name = 'creators'


class CreatorView(View):
    def get(self, request, pk):
        if Creator.objects.filter(id=pk).exists():
            return render(request, "creator.html", {"creator": Creator.objects.get(id=pk)})
        return redirect('creators')


class CreatorDetailView(DetailView):
    model = Creator
    template_name = "creator.html"
    context_object_name = "creator"


class CreatorFormView(FormView):
    template_name = "form.html"
    form_class = CreatorForm
    success_url = reverse_lazy('creators')

    def form_valid(self, form):
        result = super().form_valid(form)
        cleaned_data = form.cleaned_data
        Creator.objects.create(
            name=cleaned_data['name'],
            surname=cleaned_data['surname'],
            alias=cleaned_data['alias'],
            date_of_birth=cleaned_data['date_of_birth'],
            date_of_death=cleaned_data['date_of_death'],
            country=cleaned_data['country'],
            biography=cleaned_data['biography']
        )
        return result

    def form_invalid(self, form):
        print("Form 'CreatorForm' is invalid")
        return super().form_invalid(form)


class CountriesListView(ListView):
    template_name = "countries.html"
    model = Country
    context_object_name = 'countries'


class CountryDetailView(DetailView):
    model = Country
    template_name = "country.html"
    context_object_name = "country"
