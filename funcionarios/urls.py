from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="indexFuncionarios"),
    path("equipe/", views.UsuariosList.as_view(), name="equipe"),
    path("cadastrar/", views.UsuarioCreate.as_view(), name="cadastrar-usuario"),
    path("<int:pk>/editar", views.UsuarioUpdate.as_view(), name="editar-usuario"),
    path("<int:pk>/excluir", views.UsuarioDelete.as_view(), name="excluir-usuario"),

    path("grupos/", views.GruposList.as_view(), name="grupos"),
    path("grupo/criar", views.GrupoCreate.as_view(), name="criar-grupo"),
    path("grupo/<int:pk>/editar", views.GrupoUpdate.as_view(), name="editar-grupo"),
    path("grupo/<int:pk>/excluir", views.GrupoDelete.as_view(), name="excluir-grupo"),

]