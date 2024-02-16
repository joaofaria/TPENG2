from django.urls import path
from . import views

urlpatterns = [
    path("", views.VendaList.as_view(), name="vendas"),
    path('sistema', views.VendaView.as_view(), name='sistema'),
    path("cadastrar/", views.VendaCreate.as_view(), name="cadastrar-venda"),
    path("<int:pk>/editar", views.VendaUpdate.as_view(), name="editar-venda"),
    path("<int:pk>/excluir", views.VendaDelete.as_view(), name="excluir-venda"),

    path('buscar_produto/', views.buscar_produto, name='buscar_produto'),
    path('finalizar_venda/', views.finalizar_venda, name='finalizar_venda'),
    
    path('relatorio_vendas_dia_mes/', views.RelatorioVendasDiaMesView.as_view(), name='relatorio_vendas_dia_mes'),
    path('relatorio_vendas_funcionario_mes/', views.RelatorioVendasFuncionarioMesView.as_view(), name='relatorio_vendas_funcionario_mes'),
    path('relatorios/', views.RelatoriosView.as_view(), name='relatorios'),
]