# agenda/urls.py
from django.urls import path
from . import views # Importa as views do app agenda

urlpatterns = [
    path('', views.home, name='home'),
    path('servico/<int:servico_id>/', views.detalhe_servico, name='detalhe_servico'),
    # Nova rota para a página de sucesso do agendamento
    path('agendamento/<int:agendamento_id>/sucesso/', views.agendamento_sucesso, name='agendamento_sucesso'),
    path('agendamentos/', views.lista_agendamentos, name='lista_agendamentos'),
    # Rota para cancelar agendamento
    path('agendamento/<int:agendamento_id>/cancelar/', views.cancelar_agendamento, name='cancelar_agendamento'),
]

