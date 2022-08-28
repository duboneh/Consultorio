from django.urls import path

#Importar views criadas
from .views import PacienteCreate, AgendamentoCreate
from .views import PacienteUpdate, AgendamentoUpdate
from .views import PacienteDelete, AgendamentoDelete
from .views import PacienteList, AgendamentoList

#Padrão Django é urlpatterns
urlpatterns = [
    path('cadastrar/paciente/', PacienteCreate.as_view(), name='cadastrar-paciente'),
    path('cadastrar/agendamento/', AgendamentoCreate.as_view(), name='cadastrar-agendamento'),
    
    path('editar/paciente/<int:pk>', PacienteUpdate.as_view(), name='editar-paciente'),
    path('editar/agendamento/<int:pk>', AgendamentoUpdate.as_view(), name='editar-agendamento'),

    path('excluir/paciente/<int:pk>', PacienteDelete.as_view(), name='excluir-paciente'),
    path('excluir/agendamento/<int:pk>', AgendamentoDelete.as_view(), name='excluir-agendamento'),

    path('listar/pacientes/', PacienteList.as_view(), name='listar-pacientes'),
    path('listar/agendamentos/', AgendamentoList.as_view(), name='listar-agendamentos'),
]