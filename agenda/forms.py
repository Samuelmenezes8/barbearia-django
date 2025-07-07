# agenda/forms.py

from django import forms
from .models import Barbeiro

class AgendamentoForm(forms.Form):
    # Por padrão, required=True. Garanta que não há 'required=False' aqui.
    barbeiro = forms.ModelChoiceField(
        queryset=Barbeiro.objects.all(),
        empty_label="Selecione um barbeiro",
        label="Barbeiro"
    )
    
    # Por padrão, required=True.
    nome_cliente = forms.CharField(label="Seu Nome")

    # Por padrão, required=True.
    data_e_hora = forms.DateTimeField(
        label="Data e Hora",
        widget=forms.DateTimeInput(
            attrs={
                'id': 'datetimepicker',
                'placeholder': 'Selecione a data e hora'
            }
        )
    )