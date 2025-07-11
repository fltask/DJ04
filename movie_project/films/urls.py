from django.urls import path

from . import views

app_name = 'films'

urlpatterns = [
    path("", views.index, name="films_home"),
    path("create_review/", views.create_review, name="movie_review"),
]
