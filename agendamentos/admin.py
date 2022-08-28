from django.contrib import admin
from .models import Agendamento, Paciente

# Register your models here.
@admin.register(Agendamento)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'pagamento', 'especialidade', 'data_consulta', 'hora_consulta', 'atualizado_em')

@admin.register(Paciente)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'email', 'data_nascimento', 'celular')