# Generated by Django 5.2.3 on 2025-07-06 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendamento',
            name='data_e_hora_fim',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
