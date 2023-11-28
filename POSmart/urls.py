from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path("", views.index, name="mainIndex" ),
    path("estoque/", include("estoque.urls")),
    path('admin/', admin.site.urls),
    path("accounts/", include('django.contrib.auth.urls')),
    path("funcionarios/", include("funcionarios.urls")),
]
