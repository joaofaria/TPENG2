from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("produtos",views.produtos_view, name="produtos"),
    path("teste",views.teste, name="teste"),
]