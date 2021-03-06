from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>",views.oarticle, name="oarticle"),
    path("search/",views.search, name="search"),
    path("add/",views.add, name="add"),
    path("edit/<str:name>",views.edit, name="edit"),
    path("edit",views.saveedit, name="saveedit"),
    path("random",views.random, name="random")
]