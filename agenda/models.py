# agenda/models.py

from django.db import models

class Barbeiro(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    duracao = models.IntegerField() 

    def __str__(self):
        return f"{self.nome} - R${self.preco}"

class Agendamento(models.Model):
    # --- Verifique se estes campos existem! ---
    nome_cliente = models.CharField(max_length=200)
    data_e_hora = models.DateTimeField()
    data_e_hora_fim = models.DateTimeField(null=True, blank=True)
    
    # --- E o mais importante, as relações! ---
    barbeiro = models.ForeignKey(Barbeiro, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)

    def __str__(self):
        data_formatada = self.data_e_hora.strftime('%d/%m/%Y às %H:%M')
        return f"{self.nome_cliente} - {self.servico.nome} com {self.barbeiro.nome} em {data_formatada}"