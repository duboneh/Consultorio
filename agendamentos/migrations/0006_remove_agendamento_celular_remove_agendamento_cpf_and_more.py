# Generated by Django 4.1 on 2022-08-26 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0005_remove_paciente_agendamento_agendamento_paciente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agendamento',
            name='celular',
        ),
        migrations.RemoveField(
            model_name='agendamento',
            name='cpf',
        ),
        migrations.RemoveField(
            model_name='agendamento',
            name='data_nascimento',
        ),
        migrations.RemoveField(
            model_name='agendamento',
            name='email',
        ),
        migrations.RemoveField(
            model_name='agendamento',
            name='nome',
        ),
    ]
