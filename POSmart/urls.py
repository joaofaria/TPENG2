from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.index, name="mainIndex",),
    path("estoque/", include("estoque.urls")),
    path('admin/', admin.site.urls),
    path("accounts/", include('django.contrib.auth.urls')),
    path("funcionarios/", include("funcionarios.urls")),
    path("vendas/", include("vendas.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)