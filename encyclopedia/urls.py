from django.urls import path

from . import views

#urlpatterns = [
#    path("", views.index, name="index")
#]

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entries>",views.oarticle, name="oarticle")
]