from django.urls import path

from . import views

from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="indexEstoque"),
    # path("produtos",views.produtos_view, name="produtos"),
    path("teste",views.teste, name="teste"),
    
    path("categoria/cadastrar", views.CategoriaCreate.as_view(), name="cadastrar-categoria"),
    path("categorias", views.CategoriaList.as_view(), name="categorias"),
    path("categoria/<int:pk>/editar", views.CategoriaUpdate.as_view(), name="editar-categoria"),
    path("categoria/<int:pk>/excluir", views.CategoriaDelete.as_view(), name="excluir-categoria"),

    path("produto/cadastrar", views.ProdutoCreate.as_view(), name="cadastrar-produto"),
    path("produto/<int:pk>/editar", views.ProdutoUpdate.as_view(), name="editar-produto"),
    path("produto/<int:pk>/excluir", views.ProdutoDelete.as_view(), name="excluir-produto"),
    path("produtos", views.ProdutoList.as_view(), name="produtos"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)