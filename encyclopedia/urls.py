from django.urls import path

from . import views

#urlpatterns = [
#    path("", views.index, name="index")
#]

urlpatterns = [
    path("", views.index, name="index"),
    path("oarticle",views.oarticle, name="oarticle")
]