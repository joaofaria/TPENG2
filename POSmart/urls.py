from django.contrib import admin
from django.urls import include, path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path("", lambda request: redirect('login'), name="index_redirect"),
    path("stock/", include("stock.urls")),
    path('admin/', admin.site.urls),
    path("accounts/", include('django.contrib.auth.urls'))
]
