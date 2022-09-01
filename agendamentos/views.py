from multiprocessing import context
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from .models import Paciente, Agendamento

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin

from django.shortcuts import get_object_or_404

# Create your views here.

#CreateView#
class PacienteCreate( GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"PowerUsers"]
    model = Paciente
    fields = ['nome', 'cpf', 'data_nascimento', 'celular', 'email']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-pacientes')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Pacientes"

        return context

class AgendamentoCreate(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"PowerUsers"]
    model = Agendamento
    fields = ['paciente', 'tipo_consulta', 'pagamento', 'especialidade', 'data_consulta', 'hora_consulta']
    template_name = 'agendamentos/form.html'
    success_url = reverse_lazy('listar-agendamentos')

#UpdateView#
class PacienteUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Paciente
    fields = ['nome', 'cpf', 'data_nascimento', 'celular', 'email']
    template_name = 'cadastros/form-alterar.html'
    success_url = reverse_lazy('listar-pacientes')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Editar Cadastro de Paciente"

        return context

class AgendamentoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Agendamento
    fields = ['paciente', 'tipo_consulta', 'pagamento', 'especialidade', 'data_consulta', 'hora_consulta']
    template_name = 'agendamentos/form-alterar.html'
    success_url = reverse_lazy('listar-agendamentos')

#DeleteView#
class PacienteDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"PowerUsers"]
    model = Paciente
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy('listar-pacientes')

class AgendamentoDelete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador", u"PowerUsers"]
    model = Agendamento
    template_name = 'agendamentos/form-excluir.html'
    success_url = reverse_lazy('listar-agendamentos')

#ListView#
class PacienteList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Paciente
    template_name = 'cadastros/listas/paciente.html'

class AgendamentoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Agendamento
    template_name = 'agendamentos/listas/agendamento.html'