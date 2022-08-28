# Generated by Django 4.1 on 2022-08-26 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agendamentos', '0003_alter_agendamento_atualizado_em'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='cpf',
            field=models.CharField(help_text='Digite somente os números.', max_length=14, verbose_name='CPF '),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='data_consulta',
            field=models.DateField(help_text='DD/MM/AAAA', verbose_name='Data consulta'),
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='data_nascimento',
            field=models.DateField(help_text='DD/MM/AAAA', verbose_name='Data de Nascimento'),
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250, verbose_name='Nome do paciente')),
                ('cpf', models.CharField(help_text='Digite somente os números.', max_length=14, verbose_name='CPF ')),
                ('email', models.CharField(blank=True, max_length=250, null=True, verbose_name='E-mail')),
                ('data_nascimento', models.DateField(help_text='DD/MM/AAAA', verbose_name='Data de Nascimento')),
                ('celular', models.CharField(max_length=250, verbose_name='Núm. celular')),
                ('agendamento', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='agendamentos.agendamento')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
            },
        ),
    ]