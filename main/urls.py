from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clientes/', views.listar_clientes, name='listar_clientes'),
    path('servicos/', views.listar_servicos, name='listar_servicos'),
    path('funcionarios/', views.listar_funcionarios, name='listar_funcionarios'),
    path('atendimentos/', views.listar_atendimentos, name='listar_atendimentos'),
    path('clientes/adicionar/',views.adicionar_clientes, name='adicionar_cliente'),
    path('servicos/adicionar/',views.adicionar_servicos, name='adicionar_servico'),
    path('funcionarios/adicionar/',views.adicionar_funcionarios, name='adicionar_funcionario'),
    path('atendimentos/adicionar/',views.adicionar_atendimentos, name='adicionar_atendimentos'),
    path('clientes/editar/<int:pk>/',views.editar_cliente, name='editar_cliente'),
    path('servicos/editar/<int:pk>/',views.editar_servico, name='editar_servico'),
    path('funcionarios/editar/<int:pk>/',views.editar_funcionario, name='editar_funcionario'),
    path('atendimentos/editar/<int:pk>/',views.editar_atendimento, name='editar_atendimento'),
    path('atendimentos/remover/<int:atendimento_id>/', views.certeza_excluir_atendimento, name='certeza_excluir_atendimento'),
    path('atendimentos/remover/<int:atendimento_id>/confirmado/', views.excluir_atendimento, name='excluir_atendimento'),
]
