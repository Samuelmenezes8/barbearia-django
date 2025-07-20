# agenda/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone # Importe o timezone
from .models import Servico, Barbeiro, Agendamento
from .forms import AgendamentoForm
from datetime import timedelta

# A view da página inicial que lista os serviços
def home(request):
    lista_de_servicos = Servico.objects.all()
    contexto = {'servicos': lista_de_servicos}
    return render(request, 'agenda/home.html', contexto)

# A view da página de detalhes que mostra o formulário
def detalhe_servico(request, servico_id):
    servico = get_object_or_404(Servico, pk=servico_id)
    
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            barbeiro = form.cleaned_data['barbeiro']
            nome_cliente = form.cleaned_data['nome_cliente']
            data_e_hora = form.cleaned_data['data_e_hora']
            
            horario_inicio = data_e_hora
            duracao = servico.duracao
            horario_fim = horario_inicio + timedelta(minutes=duracao)

            agendamentos_conflitantes = Agendamento.objects.filter(
                barbeiro=barbeiro,
                data_e_hora__lt=horario_fim,
                data_e_hora_fim__gt=horario_inicio
            ).exists()

            if agendamentos_conflitantes:
                form.add_error(None, "Desculpe, este horário não está mais disponível. Por favor, escolha outro.")
            else:
                novo_agendamento = Agendamento(
                    servico=servico,
                    barbeiro=barbeiro,
                    nome_cliente=nome_cliente,
                    data_e_hora=horario_inicio,
                    data_e_hora_fim=horario_fim
                )
                novo_agendamento.save()

                messages.success(request, "Seu agendamento foi realizado com sucesso!")
                
                return redirect('agendamento_sucesso', agendamento_id=novo_agendamento.id)


    else:
        form = AgendamentoForm()

    contexto = {
        'servico': servico,
        'form': form,
    }
    return render(request, 'agenda/detalhe_servico.html', contexto)

# agenda/views.py (adicione esta nova função)

def agendamento_sucesso(request, agendamento_id):
    # Busca o agendamento específico que acabamos de criar
    agendamento = get_object_or_404(Agendamento, pk=agendamento_id)
    contexto = {
        'agendamento': agendamento,
    }
    return render(request, 'agenda/agendamento_sucesso.html', contexto)

def lista_agendamentos(request):
    # Filtra agendamentos da data/hora atual para o futuro
    # e ordena pelo mais próximo
    agendamentos = Agendamento.objects.filter(
        data_e_hora__gte=timezone.now()
    ).order_by('data_e_hora')

    contexto = {
        'agendamentos': agendamentos,
    }
    return render(request, 'agenda/lista_agendamentos.html', contexto)

def cancelar_agendamento(request, agendamento_id):
    # Por segurança, esta ação só deve ser possível via POST
    if request.method == 'POST':
        # Busca o agendamento que queremos deletar. Se não existir, retorna um erro 404.
        agendamento = get_object_or_404(Agendamento, pk=agendamento_id)
        
        # Deleta o objeto do banco de dados
        agendamento.delete()
        
        # Cria uma mensagem de feedback para o usuário
        messages.success(request, "O agendamento foi cancelado com sucesso!")
        
        # Redireciona o usuário de volta para a lista de agendamentos
        return redirect('lista_agendamentos')
    else:
        # Se alguém tentar acessar essa URL de outra forma, apenas redireciona
        return redirect('home')