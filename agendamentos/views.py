from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Paciente, Agendamento

from django.urls import reverse_lazy

from django.shortcuts import get_object_or_404

# Create your views here.

#CreateView#
class PacienteCreate(CreateView):
    model = Paciente
    fields = ['nome', 'cpf', 'email', 'data_nascimento', 'celular']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pacientes')

class AgendamentoCreate(CreateView):
    model = Agendamento
    fields = ['paciente', 'tipo_consulta', 'pagamento', 'especialidade', 'data_consulta', 'hora_consulta']
    template_name = 'agendamentos/form.html'
    success_url = reverse_lazy('listar-agendamentos')

#UpdateView#
class PacienteUpdate(UpdateView):
    model = Paciente
    fields = ['nome', 'cpf', 'email', 'data_nascimento', 'celular']
    template_name = 'cadastros/form-alterar.html'
    success_url = reverse_lazy('listar-pacientes')

class AgendamentoUpdate(UpdateView):
    model = Agendamento
    fields = ['paciente', 'tipo_consulta', 'pagamento', 'especialidade', 'data_consulta', 'hora_consulta']
    template_name = 'agendamentos/form-alterar.html'
    success_url = reverse_lazy('listar-agendamentos')

#DeleteView#
class PacienteDelete(DeleteView):
    model = Paciente
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-pacientes')

class AgendamentoDelete(DeleteView):
    model = Agendamento
    template_name = 'agendamentos/form-excluir.html'
    success_url = reverse_lazy('listar-agendamentos')

#ListView#
class PacienteList(ListView):
    model = Paciente
    template_name = 'cadastros/listas/paciente.html'

class AgendamentoList(ListView):
    model = Agendamento
    template_name = 'agendamentos/listas/agendamento.html'