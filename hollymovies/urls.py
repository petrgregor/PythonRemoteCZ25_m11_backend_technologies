"""
URL configuration for hollymovies project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from viewer.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path('movies/', movies, name='movies'),
    path('movie/<int:pk>/', movie, name='movie'),
    #path('genres/', genres, name='genres'),  # view pomocí funkce genres
    #path('genres/', GenresView.as_view(), name='genres'),  # view pomocí třídy GenresView
    #path('genres/', GenresTemplateView.as_view(), name='genres'),  # view pomocí třídy GenresTemplateView
    path('genres/', GenresListView.as_view(), name='genres'),  # view pomocí třídy GenresListView
    path('genre/<int:pk>/', genre, name='genre'),
    path('creators/', CreatorsListView.as_view(), name='creators'),
    #path('creator/<int:pk>/', CreatorView.as_view(), name='creator'),
    path('creator/<int:pk>/', CreatorDetailView.as_view(), name='creator'),
    path('creator/create/', CreatorCreateView.as_view(), name='creator_create'),
    path('creator/update/<int:pk>/', CreatorUpdateView.as_view(), name='creator_update'),
    path('creator/delete/<int:pk>/', CreatorDeleteView.as_view(), name='creator_delete'),
    #path('creatorform/', CreatorFormView.as_view(), name='creatorform'),
    path('countries/', CountriesListView.as_view(), name='countries'),
    path('country/<int:pk>/', CountryDetailView.as_view(), name='country'),
]
